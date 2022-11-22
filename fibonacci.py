"""
Music for Fibonacci
:bpm: based on the observed timing of the suspend light
"""
import phimidi as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = 'fibonacci'
bpm = 90  # beats per minute
bpM = 4  # beats per Measure
key = 'A'
root = pm.N.A3
octaves = 2
scale_type = pm.S.pentatonic_major
#  scale_type = pm.S.dorian

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

F1 = 1
F2 = 1

part = pm.Part(PROJECT, 'music_for_fib', bpm=bpm, root=root, key=key)
b = part.ticks_per_beat
M = bpM * part.ticks_per_beat  # ticks per Measure

tracks = []
limit = 377

scale = reversed(scale)

for i, note in enumerate(scale):
    if F2 > 8:
        inst = part.add_choir_swell()
        note -= 12
        velocity = 60
    else:
        inst = part.add_vibes()
        note += 12
        velocity = 30
        #  inst = part.add_choir_swell()

    for _ in range(int(limit/(F1 + F2))):
        inst.set_rest(F2 * b)
        inst.set_note(note, F1 * b, velocity=velocity)

        if F2 > 8:
            inst.ramp_volume_up(F2 * b)
            inst.ramp_volume_down(F1 * b)

    F1, F2 = F2, F1 + F2

part.save()
part.play()
#  part.convert()
    
