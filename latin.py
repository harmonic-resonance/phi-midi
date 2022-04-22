import phimidi as pm
import math as math
import subprocess as subprocess


PROJECT = 'phi-midi'
NAME = 'latin'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

pulse = 120
tempo = pm.bpm2tempo(pulse)
mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat

tick = pm.Percussion(mf, pm.P.side_stick)
kick = pm.Percussion(mf, pm.P.acoustic_bass_drum)
snare = pm.Percussion(mf, pm.P.acoustic_snare)
hihat_closed = pm.Percussion(mf, pm.P.closed_hi_hat)
ride = pm.Percussion(mf, pm.P.ride_cymbal_1)

# count
kick.set_rest(M)
#  snare.set_rest(M)
#  hihat_closed.set_rest(M)
ride.set_rest(M)
mf.tracks[0].append(pm.MetaMessage('marker', text='count', time=0))
tick.set_hits(M, 4, velocity=40)

mf.tracks[0].append(pm.MetaMessage('marker', text='son_clave', time=M))
for _ in range(4):
    pm.patterns.latin.son_clave(M, kick, tick, ride)

mf.tracks[0].append(pm.MetaMessage('marker', text='bossa nova', time=M))
for _ in range(4):
    pm.patterns.latin.bossa_nova(M, kick, tick, ride)

mf.tracks[0].append(pm.MetaMessage('marker', text='rhumba', time=M))
for _ in range(4):
    pm.patterns.latin.rhumba(M, kick, tick, ride)

filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", '-in', '-c', '~/.photon/timidity.cfg', filepath])
