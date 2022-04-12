import phimidi as pm
import math as math
import subprocess as subprocess


PROJECT = 'phi-midi'
NAME = 'drums'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

pulse = 120
tempo = pm.bpm2tempo(pulse)
mf = pm.new_midi(title=title, tempo=tempo)
M = 4 * mf.ticks_per_beat


kick = pm.Percussion(mf, pm.P.acoustic_bass_drum)
snare = pm.Percussion(mf, pm.P.acoustic_snare)
tick = pm.Percussion(mf, pm.P.side_stick)
hihat_closed = pm.Percussion(mf, pm.P.closed_hi_hat)
ride = pm.Percussion(mf, pm.P.ride_cymbal_1)

#  kicks = 8

#  for i in range(kicks):
    #  kick.set_hit(480, velocity=100)
    #  if i > 1:
        #  for _ in range(4):
            #  snare.set_hit(120, velocity=40)
        #  for _ in range(12):
            #  tick.set_hit(40, velocity=20)
    #  else:
        #  snare.set_rest(480)
        #  tick.set_rest(480)
        
# count
for _ in range(4):
    tick.set_hit(M/4, velocity=40)

kick.set_rest(M)
snare.set_rest(M)
hihat_closed.set_rest(M)
for _ in range(4):
    kick.set_hit(M/2, velocity=100)
    kick.set_hit(M/2, velocity=80)
    for _ in range(2):
        snare.set_rest(M/4)
        snare.set_hit(M/4)
    for _ in range(8):
        hihat_closed.set_hit(M/8)


ride.set_rest(5 * M)
for _ in range(8):
    kick.set_hit(5 * M/12)
    kick.set_hit(M/12)
    #  kick.set_rest(M/4)
    ride.set_hit(M/4)
    ride.set_hit(M/6)
    ride.set_hit(M/12)

ride.set_hit(M)

filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", filepath])
