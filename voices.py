'''
voices are contained in the KBH_Real_and_Swell_Choir.sf2 soundfont

timidity requires voices.cfg file to establish voices on bank 1
'''

import phimidi as pm
import subprocess as subprocess


PROJECT = 'phi-midi'
NAME = 'voices'

M = 1920

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

mf = pm.new_midi(title=title)
   
solo_ooh = pm.Voice(mf, voice_name='Solo Ooh')

#  solo_ooh.set_note(72, duration=M)

swell = pm.Voice(mf, voice_name=pm.V.choir_mixed)
#  swell.set_rest(M)
swell.set_chord(60, M*2, chord_type=pm.C.major)
swell.set_chord(67, M*2, chord_type=pm.C.major_7)
swell.set_chord(64, M*2, chord_type=pm.C.major_7)
swell.set_chord(60, M*2, chord_type=pm.C.sus2)

filepath = pm.save_midi(mf, folder, filename)

mf.print_tracks()

#  !timidity -c voices.cfg $filename
subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
