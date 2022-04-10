import phi_midi as pm
import math as math
import subprocess as subprocess

tempo=250000*4
pulse=120


filename = f'drums.mid'
mf = pm.new_midi(title=filename)
mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=0))

kick = pm.set_new_track(mf, name='kick')
kick.append(pm.Message('program_change', channel=9, time=0))

snare = pm.set_new_track(mf, name='snare')
snare.append(pm.Message('program_change', channel=9, time=0))

tick = pm.set_new_track(mf, name='tick')
tick.append(pm.Message('program_change', channel=9, time=0))



kicks = 8

#  root -= 12

for i in range(kicks):
    pm.set_note(kick, 35, channel=9, duration=480)
    if i > 1:
        for _ in range(4):
            pm.set_note(snare, 38, channel=9, velocity=30, duration=120)
        for _ in range(12):
            pm.set_note(tick, 37, channel=9, velocity=30, duration=40)
    else:
        pm.set_note(snare, 0, channel=9, duration=480)
        pm.set_note(tick, 0, channel=9, duration=480)
        



filepath = f'out/{filename}'
mf.save(filepath)

subprocess.run(["timidity", filepath])
