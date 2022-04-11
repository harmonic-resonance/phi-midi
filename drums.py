import phimidi as pm
import math as math
import subprocess as subprocess

tempo=250000*4
pulse=120

PROJECT = 'phi-midi'
NAME = 'drums'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

mf = pm.new_midi(title=title, tempo=tempo)
#  mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=0))

kick = pm.Percussion(mf, pm.P.acoustic_bass_drum)
snare = pm.Percussion(mf, pm.P.acoustic_snare)
tick = pm.Percussion(mf, pm.P.side_stick)

kicks = 8

for i in range(kicks):
    kick.set_hit(480, velocity=100)
    if i > 1:
        for _ in range(4):
            snare.set_hit(120, velocity=40)
        for _ in range(12):
            tick.set_hit(40, velocity=20)
    else:
        snare.set_rest(480)
        tick.set_rest(480)
        
filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", filepath])
