import phimidi as pm
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

PROJECT = 'phi-midi'
NAME = 'spirals'
filename = f'{scale_type}-{n}-{octaves}.mid'

folder = f'{PROJECT}/{NAME}'
title = f'{PROJECT} - {NAME}'

filename = f'{scale_type}-{n}-{octaves}.mid'
mf = pm.new_midi(title=filename, tempo=tempo)

vibes = pm.Instrument(mf, pm.I.vibraphone, 1)
bass = pm.Instrument(mf, pm.I.acoustic_bass, 2)
v1 = pm.Voice(mf, voice_name=pm.V.choir_ooh)
v2 = pm.Voice(mf, voice_name=pm.V.choir_aah)

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

v1.set_rest(pulse*13)
v2.set_rest(pulse*21)

for i, note in enumerate(notes):
    #  vibes.append(pm.Message('control_change', control=10, value=pans[i], time=0))
    offset = 0
    if i < len(offsets):
      offset = offsets[i] * pulse
    vibes.set_note(note, duration=offset+pulse)
    if i % 21 == 13:
        v1.set_note(note, duration=pulse*21)
    if i % 34 == 21:
        v2.set_note(note, duration=pulse*34)

filepath = pm.save_midi(mf, folder, filename)

mf.print_tracks()

subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", "-c", "voices.cfg", filepath])
