import phi_midi as pm
import math as math
import subprocess as subprocess

n = 144
root = 48
octaves = 3
scale_type = 'dorian'
scale_type = 'pentatonicmajor'
#  scale_type = 'harmonicminor'
# scale_type = 'ionian'
# scale_type = 'bluesmajor'
tempo=250000*4
pulse=120

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

filename = f'{scale_type}-{n}-{octaves}.mid'
mf = pm.new_midi(title=filename)
mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=0))

vibes = pm.set_new_track(mf, name='vibes')
vibes.append(pm.Message('program_change', program=11, time=0))

gong = pm.set_new_track(mf, name='gong')
gong.append(pm.Message('program_change', program=32, channel=1, time=0))

v1 = pm.add_voice_track(mf, name='Mixed Choir')
v2 = pm.add_voice_track(mf, name='Swell Choir')


phi = (1 + math.sqrt(5)) / 2
angle = (2 * math.pi) / phi
angles = []

print('phi:', phi)
print('angle:', angle)
print('scale:', scale)

for i in range(n):
    theta = angle * i
    angles.append(theta)
    
sins = list(map(lambda x: math.sin(x), angles))
coss = list(map(lambda x: math.cos(x), angles))

def get_note(x):
    '''range -1 to 1'''
    divs = len(scale)
    i = int((x+1)/2 * divs)
    return scale[i]
    
def get_pan(x):
    '''range -1 to 1'''
    divs = 127
    i = int((x+1)/2 * divs)
    return i
    
notes = list(map(get_note, sins))
pans = list(map(get_pan, coss))

offsets = [1, 1, 2, 3, 5, 8] #, 13, 21, 34, 55]
offsets = list(reversed(offsets))

pm.add_voice_note(v1, 0, duration=pulse*13)
pm.add_voice_note(v2, 0, duration=pulse*21)
for i, note in enumerate(notes):
    vibes.append(pm.Message('control_change', control=10, value=pans[i], time=0))
    offset = 0
    if i < len(offsets):
      offset = offsets[i] * pulse
    pm.set_note(vibes, note, duration=offset+pulse)
    if i % 21 == 13:
        pm.add_voice_note(v1, note, duration=pulse*21)
    if i % 34 == 21:
        pm.add_voice_note(v2, note, duration=pulse*34)
        # pm.add_voice_chord(v1, 60, duration=1920*2, chord=pm.CHORDS['Major7'])


gongs = int(n / octaves)
gong_gap = octaves * pulse

#  root -= 12

#  for i in range(gongs):
    #  if i > gongs/phi:
        #  pm.set_note(gong, root+12, channel=1, duration=gong_gap)
    #  else:
        #  pm.set_note(gong, root, channel=1, duration=gong_gap)

filepath = f'out/{filename}'
mf.save(filepath)

#  !timidity -c voices.cfg $filename
subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
