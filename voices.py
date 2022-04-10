import phimidi as pm
import subprocess as subprocess


PROJECT = 'phi-midi'
NAME = 'voices'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

mf = pm.new_midi(title=title)
   

v1 = pm.add_voice_track(mf, name='Solo Ooh')
v2 = pm.add_voice_track(mf, name='Swell Choir')

pm.add_voice_note(v1, 72, duration=1920)
pm.add_voice_note(v1, 70, duration=1920)

pm.add_voice_chord(v1, 60, duration=1920*2, chord=pm.CHORDS['Major7'])

pm.add_voice_note(v2, 0, duration=1920*3)
pm.add_voice_note(v2, 72, duration=1920)
pm.add_voice_chord(v2, 60, duration=1920*2, chord=pm.CHORDS['Sus2'])
pm.add_voice_note(v2, 69, duration=1920)


#  mf.save('voices.mid')

#  !timidity -c voices.cfg voices.mid
filepath = pm.save_midi(mf, folder, filename)

mf.print_tracks()

#  !timidity -c voices.cfg $filename
subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
