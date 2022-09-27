"""
script for generating accompaniment for Thelio videos
:bpm: based on the observed timing of the suspend light
"""
import phimidi as pm
import math as math
import subprocess as subprocess
import numpy as np
import itertools as itertools
import random as random

PROJECT = 'phi-midi'
NAME = 'thelio'
#  NAME = 'thelio-corners'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 88  # beats per minute
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.D3

#  octaves = 2
#  scale_type = pm.S.dorian
#  scale_type = pm.S.pentatonic_major

#  scale = pm.build_scale(
    #  root=root,
    #  scale_type=scale_type,
    #  octaves=octaves)

#  perms = list(itertools.combinations(scale, 4))
#  random.shuffle(perms)

# create new midi session
mf = pm.new_midi(title=title, tempo=tempo)

bpM = 4  # beats per Measure
M = bpM * mf.ticks_per_beat  # ticks per Measure

vibes = pm.make_vibes(mf, 1)
bass = pm.make_bass(mf, 2)
#  horns = pm.make_horns(mf, 3)
strings = pm.make_strings(mf, 4)

#  kick = pm.make_kick(mf)
#  snare = pm.make_snare(mf)
#  ride = pm.make_ride(mf)
#  tick = pm.make_tick(mf)
#  hihat_closed = pm.make_hihat_closed(mf)

choir = pm.make_choir_swell(mf)
#  solo = pm.make_solo_aah(mf)

# create numpy array for volume steps
# results in 16 steps
steps = np.arange(32, 96, 4)
print(f'steps: {len(steps)}')
print(steps)

#  chords = pm.progressions.i_vi_ii_V(root)
chords = pm.progressions.p5(root)

for verse in range(1):
    # each cord is held for 4 measures
    for chord_num, chord in enumerate(chords):
        # bass, horn, drum loops
        # bass, drums fill on 4
        measures = 8
        for m in range(measures):
            if m == measures - 1:
                # fill
                bass.set_note(root, M, velocity=80)

                # swap ride and snare
                #  pm.patterns.techno.drum_bass(M, kick, ride, hihat_closed, snare )
                #  pm.patterns.latin.rhumba(M, ride, tick, kick)
            else:
                bass.set_note(root - 12, M, velocity=90)

                #  pm.patterns.techno.drum_bass(M, kick, snare, hihat_closed, ride)
                #  pm.patterns.latin.rhumba(M, kick, tick, ride)

        choir.set_rest(M)
        choir.set_volume(steps[0], M)
        choir.set_notes(chord, (measures - 1) * M)
        for val in steps:
            choir.set_volume(val, 1 * M/len(steps))

        for val in reversed(steps):
            choir.set_volume(val, (measures - 2) * M/len(steps))

        #vibes
        #  vibes.set_volume(steps[0], 0)
        chord2 = [note + 12 for note in chord]
        chord3 = [note + 12 for note in chord2]
        chord4 = [note + 12 for note in chord3]

        offset = M/32
        vibes.set_rest(2 * M)
        vibes.set_notes(chord3, M, offset=offset, velocity=55)
        vibes.set_notes(chord4, M/2, offset=offset, velocity=65)
        vibes.set_notes(chord4, 4*M + M/2, offset=offset, velocity=65)
        #  vibes.set_notes(chord, M/4, velocity=70)
        #  vibes.set_notes(chord2, M/4, velocity=80)
        #  #  pm.add_arp_up(vibes, chord, M)
        #  #  pm.add_arp_down(vibes, chord, M)
        #  vibes.set_rest(M)

        #  for val in steps:
            #  vibes.set_volume(val, 4 * M/len(steps))

        # strings
        #  if verse == 0:
        if verse > 0:
            strings.set_rest(4 * M)
            strings.set_notes(chord, 4 * M, M / 8)
            #  strings.set_notes(chord, 2 * M, M / 2)
        else:
            strings.set_rest(measures * M)

        strings.set_volume(steps[0], 4 * M)
        for val in steps:
            strings.set_volume(val, M/len(steps))
        for val in reversed(steps):
            strings.set_volume(val, 3 * M/len(steps))

        # solo
        if verse > 2:
            solo.set_rest(M/4)
            solo.set_note(chord[0], 3 * M/4)
            solo.set_note(chord[2], 1 * M/4)
            solo.set_rest(M/4)
            solo.set_note(chord[2], 2 * M/4)
            solo.set_note(chord[1], 1 * M/4)
            solo.set_rest(M/4)
            solo.set_note(chord[0], 1 * M/4)
            solo.set_note(chord[2], 5 * M/4)
        else:
            solo.set_rest(4 * M)



filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath])
subprocess.run(["timidity", '-in', "-c", "~/.photon/timidity.cfg", filepath, '-Ov'])
