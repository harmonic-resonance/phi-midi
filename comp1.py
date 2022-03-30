import phi_midi as pm
import math as math
import subprocess as subprocess

root = 48
octaves = 3
scale_type = 'pentatonicmajor'
tempo=250000*4

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

filename = f'comp1.mid'
mf = pm.new_midi(title=filename)
mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=0))

vb = pm.Instrument(mf, "Vibraphone", 1)
vb.set_note(60, 480)
vb.set_note(64, 480)
vb.set_note(67, 960)

vb.set_note(60, 480)
vb.set_rest(480)
vb.set_note(67, 960)

vb.set_note(60, 480)
vb.set_rest(480)
vb.set_note(67, 960)

vb.set_chord(60, 960)
vb.set_chord(65, 960)
vb.set_chord(60, 960)
vb.set_chord(65, 960)
vb.set_chord(60, 960)
vb.set_chord(65, 960)
vb.set_chord(67, 1920)

#  vb.set_volume(30, 0)
#  for i in range(10,128):
    #  vb.set_volume(i, 30)

bass = pm.Instrument(mf, 'Acoustic Bass', 2)
bass.set_rest(1920)
bass.set_rest(1920)
bass.set_rest(1920)

bass.set_note(48, 480)
bass.set_note(48, 240)
bass.set_note(55, 240)
bass.set_rest(960)

bass.set_note(48, 480)
bass.set_note(48, 240)
bass.set_note(55, 240)
bass.set_rest(960)

bass.set_note(48, 480)
bass.set_note(48, 240)
bass.set_note(55, 240)
bass.set_rest(960)

bass.set_note(48, 480)
bass.set_note(57, 240)
bass.set_note(57, 240)
bass.set_note(48, 480)
bass.set_note(57, 240)
bass.set_note(57, 240)

#  v1 = pm.add_voice_track(mf, name='Mixed Choir')
#  v2 = pm.add_voice_track(mf, name='Swell Choir')


filepath = f'out/{filename}'
mf.save(filepath)

mf.print_tracks()

#  !timidity -c voices.cfg $filename
subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
