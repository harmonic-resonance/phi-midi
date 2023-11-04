"""
phimidi template
"""
import phimidi as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = 'demos'
title = 'template'
bpm = 88  # beats per minute
bpM = 4  # beats per Measure
root = pm.N.D3  # the root note of the key
key = 'D'

part = pm.Part(PROJECT, title, bpm=bpm, root=root, key=key)
M = bpM * part.ticks_per_beat  # ticks per Measure

chords = pm.progressions.ii_V_i_i(root)

vibes = part.add_vibes()
bass = part.add_bass()
strings = part.add_strings()

# kit
kick = pm.make_kick(part)
ride = pm.make_ride(part)
#  tick = pm.make_tick(part)
tick = pm.make_low_tom(part)

choir = part.add_choir_swell()

for chord_num, (chord_name, chord) in enumerate(chords):
    if chord_num in [0, 3]:
        rhythm = pm.patterns.latin.bossa_nova
    if chord_num in [1, 4]:
        rhythm = pm.patterns.latin.rhumba
    if chord_num in [2, 5]:
        rhythm = pm.patterns.latin.son_clave
    measures = 4
    for m in range(measures):
        if m == 0:
            # first
            bass.set_note(root - 12, M, velocity=90)
            kick.set_rest(M)
            ride.set_rest(M)
            tick.set_hits(M, 4, velocity=30)
        elif m == measures - 1:
            # last
            bass.set_note(root, M, velocity=80)

            rhythm(M, ride, tick, kick, velocity_mod=-30)
        else:
            bass.set_note(root - 12, M, velocity=90)

            velocity_mod = -40 if m % 2 else -20
            rhythm(M, kick, tick, ride, velocity_mod=velocity_mod)

    choir.set_rest(M)
    choir.set_notes(chord, (measures - 1) * M)
    choir.set_volume(32, M)
    choir.ramp_volume_up(M)
    choir.ramp_volume_down((measures - 2) * M)

    chord2 = [note + 12 for note in chord]
    chord3 = [note + 12 for note in chord2]
    chord4 = [note + 12 for note in chord3]

    offset = M/32
    vibes.set_rest(2 * M)
    vibes.set_notes(chord3, M, offset=offset, velocity=55)
    vibes.set_notes(chord4, M/2, offset=offset, velocity=65)
    vibes.set_notes(chord4, M/2, offset=offset, velocity=65)
    #  vibes.set_notes(chord4, 4*M + M/2, offset=offset, velocity=65)

    # strings
    #  if chord_num in [0, 3]:
        #  strings.set_rest(4 * M)
        #  strings.set_notes(chord, 4 * M, M / 8)
        #  #  strings.set_notes(chord, 2 * M, M / 2)
    #  else:
        #  strings.set_rest(measures * M)

    #  strings.set_volume(32, 4 * M)
    #  strings.ramp_volume_up(M)
    #  strings.ramp_volume_down(3 * M)

part.save()
part.play()
#  part.convert()

