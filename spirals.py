import phimidi as pm
import math as math
import subprocess as subprocess

phi = (1 + math.sqrt(5)) / 2
#  angle = (2 * math.pi) - ((2 * math.pi) / phi)
angle = (2 * math.pi) - ((2 * math.pi) / phi)
#  angle = (2 * math.pi) - ((2 * math.pi) / 144/89)
angles = []

print('phi:', phi)
print('angle:', angle)
print('degrees:', math.degrees(angle))
print()

# number of nodes
n = 144
n = 610
# relating to color cycles in plot
cycles = 6

bpm = 60
tempo = int(pm.bpm2tempo(bpm))

root =  pm.N.E3
scale_type = pm.S.harmonic_minor
scale_type = pm.S.melodic_minor
scale_type = pm.S.dorian
#  scale_type = pm.S.pentatonic_minor
#  scale_type = pm.S.pentatonic_major
octaves = 2

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)
#  scale = pm.get_chord_notes(root, pm.C.dominant_7)
#  scale.extend(pm.get_chord_notes(root + 12, pm.C.dominant_7))
#  scale.extend(pm.get_chord_notes(root + 24, pm.C.dominant_7))
print('scale:', scale)

PROJECT = 'phi-midi'
NAME = 'spirals'
filename = f'{scale_type}-{n}-{octaves}.mid'

folder = f'{PROJECT}/{NAME}'
title = f'{PROJECT} - {NAME}'

filename = f'{scale_type}-{n}-{cycles}.mid'
mf = pm.new_midi(title=filename, tempo=tempo)
beat=mf.ticks_per_beat
#  M = 4 * beat

vibes = pm.make_vibes(mf, 1)
bass = pm.make_bass(mf, 2)
horns = pm.make_horns(mf, 3)
v1 = pm.make_choir_swell(mf)


for i in range(n):
    theta = angle * i
    angles.append(theta)
    
print(angles)
print()


sins = list(map(lambda a: math.sin(a), angles))
coss = list(map(lambda a: math.cos(a), angles))

def get_note_linear(x):
    '''range -1 to 1'''
    divs = len(scale)
    i = int((x+1)/2 * divs)
    return scale[i]
    
def get_note_circle(angle):
    divs = math.pi * 2 / len(scale)
    angle = angle % (2 * math.pi)
    i = int(angle / divs)
    note = scale[i]
    print(angle, i, note)
    return note
    
def get_pan(x):
    '''range -1 to 1'''
    divs = 127
    i = int((x+1)/2 * divs)
    return i
    
notes = list(map(get_note_circle, angles))
pans = list(map(get_pan, coss))

offsets = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
offsets.append(144)
#  offsets = list(reversed(offsets))

#  v1.set_rest(beat*13)
#  v2.set_rest(beat*21)

vibes.set_volume(60, 0)
v1.set_volume(90, 0)
horns.set_volume(40, 0)
for i in range(n):
    #  level = int(30 + ((i/n) * 60)) 
    level = int(70 - ((i/n) * 60)) 
    bass.set_volume(level, beat)
    bass.set_note(root - 12, duration=beat/2, velocity=60)
    bass.set_note(root - 24, duration=beat/2, velocity=20)

for i, note in enumerate(notes):
    vibes.set_pan(pans[i], 0)
    offset = 0
    #  if i < len(offsets):
      #  offset = offsets[i] * beat
    vibes.set_note(24 + note, duration=beat)
    if i % cycles == 0:
        d = cycles * beat
        v1.set_note(note, duration=d-beat)
        v1.set_rest(beat)
        v1.set_volume(20, 0)
        for i in range(8):
            level = 20 + (i) * 8
            #  level = i * 4 + 20
            v1.set_volume(level, d/24)
        for i in reversed(range(16)):
            level = 20 + (i) * 4
            #  level = i * 4 + 20
            v1.set_volume(level, d/24)
    if i in offsets:
        d = i * beat
        new_bpm = bpm + (4 *i)
        tempo = int(pm.bpm2tempo(new_bpm))
        
        mf.tracks[0].append(pm.MetaMessage('set_tempo', tempo=tempo, time=d))
        horns.set_note(note - 12, duration=d-beat)
        horns.set_rest(beat)
        horns.set_volume(10, 0)
        for i in range(8):
            level = (i) * 8 + 10
            #  level = i * 4 + 20
            horns.set_volume(level, d/24)
        for i in reversed(range(16)):
            level = (i) * 4 + 10
            #  level = i * 4 + 20
            horns.set_volume(level, d/24)

    #  if i % 21 == 13:
        #  v1.set_note(note, duration=beat*21)
    #  if i % 34 == 21:
        #  v2.set_note(note, duration=beat*34)

filepath = pm.save_midi(mf, folder, filename)

#  mf.print_tracks()

#  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
subprocess.run(["timidity", '-in', "-c", "voices.cfg", filepath])
#  subprocess.run(["timidity", filepath])
