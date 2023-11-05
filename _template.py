"""
phimidi template
"""
import phimidi as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = 'demos'
title = 'template'
bpm = 120 # beats per minute
bpM = 4  # beats per Measure
root = pm.N.D3  # the root note of the key
key = 'D'

part = pm.Part(PROJECT, title, bpm=bpm, root=root, key=key)
M = bpM * part.ticks_per_beat  # ticks per Measure

chords = pm.progressions.ii_V_i_i(root)
chords = pm.progressions.i_vi_ii_V(root)

piano = part.add_piano()
vibes = part.add_vibes()
bass = part.add_bass()
strings = part.add_strings()

# kit
#  kick = pm.make_kick(part)
#  ride = pm.make_ride(part)
#  tick = pm.make_tick(part)
#  tick = pm.make_low_tom(part)

choir = part.add_choir_swell()

conga = pm.Conga(part)
standard = pm.Standard(part)


for loop in range(4):
    part.set_marker(f'{loop}', 0)
    for chord_num, (chord_name, chord) in enumerate(chords):
        chord2 = [note + 12 for note in chord]
        chord3 = [note + 12 for note in chord2]
        chord4 = [note + 12 for note in chord3]

        part.set_marker(f'{chord_name} - {chord}', 0)

        if chord_num in [0, 2]:
            rhythm = pm.patterns.latin.bossa_nova
        if chord_num in [1, 3]:
            rhythm = pm.patterns.latin.rhumba

        rhythm = pm.patterns.funky.billie_jean

        measures = 4
        for m in range(measures):
            part.set_marker(f'{m + 1}', M)
            #  if m == 0:
                #  velocity_mod = 10 
                #  #  conga.samba(2 * M, velocity_mod=-10)
                #  standard.billie_jean(2 * M, velocity_mod=-10)
            #  elif m == 2:
                #  standard.billie_jean(2 * M, velocity_mod=-10)
            #  else:
                #  pass
            standard.funky_drummer(M, velocity_mod=-10)

            if chord_num == 3:
                if m == measures - 1:
                    # last
                    bass.set_note(chord[1] - 12, M, velocity=90)
                else:
                    bass.set_note(chord[2] - 12, M, velocity=70)
            else:
                if m == measures - 1:
                    # last
                    bass.set_note(chord[1] - 12, M, velocity=90)
                else:
                    bass.set_note(chord[0] - 12, M, velocity=70)

            if loop > 0:
                if chord_num == 3:
                    # last
                    piano.set_notes(chord2, M, velocity=60)
                else:
                    piano.set_notes(chord, M, velocity=60)
            else:
                piano.set_rest(M)


        #  if loop > 2:
            #  velocity_mod = 10 
            #  rhythm(2 * M, kick, tick, ride, velocity_mod=velocity_mod)
            #  velocity_mod = -10 
            #  rhythm(2 * M, kick, tick, ride, velocity_mod=velocity_mod)
        #  else:
            #  kick.set_rest(4 * M)
            #  ride.set_rest(4 * M)
            #  tick.set_rest(4 * M)

        if loop > 2:
            strings.set_rest(3 * M)
            strings.set_notes(chord2, M/2, velocity=20)
            strings.set_notes(chord3, M/2, velocity=30)
        else:
            strings.set_rest(4 * M)

        if loop > 1:
            #  choir.set_rest(M)
            #  choir.set_notes(chord, (measures - 1) * M, offset=M/8)
            if chord_num == 3:
                choir.set_rest(4 * M)
                choir.set_volume(32, 4 * M)
            else:
                choir.set_notes(chord, measures  * M, offset=M/4)
                choir.set_volume(32, 0)
                choir.ramp_volume_up(2 * M)
                choir.ramp_volume_down(2 * M)
        else:
            choir.set_rest(4 * M)
            choir.set_volume(32, 4 * M)


        #  offset = M/32
        #  #  vibes.set_rst(2 * M)
        #  vibes.set_notes(chord3, 3 * M, offset=offset, velocity=55)
        #  vibes.set_notes(chord4, M/2, offset=offset, velocity=65)
        #  vibes.set_notes(chord4, M/2, offset=offset, velocity=65)

        #  #  strings
        #  if chord_num in [2, 3]:
            #  strings.set_rest(2 * M)
            #  strings.set_notes(chord, 2 * M, M / 8)
        #  else:
            #  strings.set_rest(measures * M)

        #  strings.set_volume(32, 2 * M)
        #  strings.ramp_volume_up(2 * M)

part.save()
part.play()
#  part.convert()

