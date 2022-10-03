"""
script for generating accompaniment for Thelio videos
:bpm: based on the observed timing of the suspend light
"""
import phimidi as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = 'test_patterns'
bpm = 180  # beats per minute
bpM = 4  # beats per Measure
root = pm.N.D3  # the root note of the key
key = 'D'

part = pm.Part(PROJECT, 'son_clave', bpm=bpm, root=root, key=key)
M = bpM * part.ticks_per_beat  # ticks per Measure

kick = part.add_kick()
#  snare = pm.make_snare(part)
#  ride = pm.make_ride(part)
#  tick = pm.make_tick(part)
#  low_tom = pm.make_low_tom(part)
#  high_tom = pm.make_high_tom(part)
clave = pm.Percussion(part, pm.P.claves)

part.set_marker(f'count', 0)
clave.set_hits(M, 4)
kick.set_rest(M)

for i in range(4):
    dur = 4 * M if i else M
    part.set_marker(f'{i}', dur)
    #  kick.set_marker('kick', duration=4*M)
    kick.set_hits(4 * M, 4)
    pm.patterns.latin.son_clave2(2 * M, clave)
    pm.patterns.latin.son_clave2(2 * M, clave, velocity_mod=40)

part.save()
part.play()
