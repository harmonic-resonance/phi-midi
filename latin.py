import phimidi as pm
import math as math
import subprocess as subprocess

def hold_4(dur,  kick, tick, ride):
    tick.set_hits(dur, 4, velocity=40)
    kick.set_hits(dur, 2, velocity=60)
    ride.set_hits(dur, 8, velocity=40)

#  def set_marker(mf, text, dur):
    #  """
    #  set marker at zero then blank marker with duration
    #  """
    #  mf.tracks[0].append(pm.MetaMessage('marker', text=text, time=0))
    #  mf.tracks[0].append(pm.MetaMessage('marker', text='', time=dur))


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
#  mf.tracks[0].append(pm.MetaMessage('marker', text='count', time=0))
set_marker(mf, 'count', 0)
kick.set_rest(M)
#  snare.set_rest(M)
#  hihat_closed.set_rest(M)
ride.set_rest(M)
tick.set_hits(M, 4, velocity=40)

measures = 4

set_marker(mf, 'son_clave', M)
for i in range(measures):
    if i < 3:
        pm.patterns.latin.son_clave(M, kick, tick, ride)
    else:
        pm.patterns.latin.son_clave(M, tick, kick, ride)
hold_4(M, kick, tick, ride)

set_marker(mf, 'bossa_nova', measures * M)
for i in range(measures):
    if i < 3:
        pm.patterns.latin.bossa_nova(M, kick, tick, ride)
    else:
        pm.patterns.latin.bossa_nova(M, tick, kick, ride)
hold_4(M, kick, tick, ride)

set_marker(mf, 'rhumba', measures * M)
for i in range(measures):
    pm.patterns.latin.rhumba(M, kick, tick, ride)
hold_4(M, kick, tick, ride)

filepath = pm.save_midi(mf, folder, filename)

subprocess.run(["timidity", '-in', '-c', '~/.photon/timidity.cfg', filepath])
