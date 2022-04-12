'''
voices are contained in the KBH_Real_and_Swell_Choir.sf2 soundfont

timidity requires voices.cfg file to establish voices on bank 1
'''
import phimidi as pm
import subprocess as subprocess

PROJECT = 'phi-midi'
NAME = 'voices'

folder = f'{PROJECT}/{NAME}'
filename = f'{NAME}.mid'
title = f'{PROJECT} - {NAME}'

bpm = 120
tempo = int(pm.bpm2tempo(bpm))

root = pm.N.D3
octaves = 3
scale_type = pm.S.dorian

scale = pm.build_scale(
    root=root, 
    scale_type=scale_type, 
    octaves=octaves)

mf = pm.new_midi(title=title, tempo=tempo)
# one measure in ticks
M = 4 * mf.ticks_per_beat

   

EBCsA = [
        (pm.N.E4, M, pm.C.major_7),
        (pm.N.B3, M, pm.C.major_7),
        (pm.N.Cs4, M, pm.C.minor_7),
        (pm.N.A3, M, pm.C.major_7),
        ]
EAGsABE = [
        (pm.N.E4, M/2, pm.C.major_7),
        (pm.N.A4, M/2, pm.C.major_7),
        (pm.N.Gs4, M, pm.C.minor_7),
        (pm.N.A4, M/2, pm.C.major_7),
        (pm.N.B4, M/2, pm.C.major_7),
        (pm.N.E3, M, pm.C.major_7),
        ]
p3 = []
chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.C3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.D3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.E3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.F4, pm.C.major)
chord.append(pm.N.F3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.G3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.F4, pm.C.major)
chord.append(pm.N.A3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.B3)
p3.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
p3.append(chord)

##########################
p4 = []
chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.G4, pm.C.major)
chord.append(pm.N.B3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.A4, pm.C.minor)
chord.append(pm.N.A3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.A4, pm.C.minor)
chord.append(pm.N.G3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.F4, pm.C.major)
chord.append(pm.N.F3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.E3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.D4, pm.C.minor_7)
chord.append(pm.N.D3)
p4.append(chord)

chord = pm.get_chord_notes(pm.N.C4, pm.C.major)
chord.append(pm.N.C3)
p4.append(chord)

#####################

p5 = [
        (pm.N.C4, M, pm.C.major),
        (pm.N.A4, M, pm.C.major_7),
        (pm.N.D4, M, pm.C.major_7),
        (pm.N.G4, M, pm.C.major),
        (pm.N.C4, M, pm.C.major),
        ]

main = pm.make_choir_swell(mf)

for _ in range(1):
    for root, duration, chord_type in EBCsA:
        main.set_chord(root, duration, chord_type=chord_type)
    main.set_rest(M)

for _ in range(1):
    for root, duration, chord_type in EAGsABE:
        main.set_chord(root, duration, chord_type=chord_type)
    main.set_rest(M)

main = pm.Instrument(mf, pm.I.vibraphone, 0)

r = pm.second2tick(mf.length, mf.ticks_per_beat, tempo)
main.set_rest(r)

for _ in range(1):
    for root, duration, chord_type in p5:
        main.set_chord(root, duration, chord_type=chord_type)
    main.set_rest(M)


for _ in range(1):
    for chord in p3:
        main.set_notes(chord, M)
    main.set_rest(M)

for _ in range(1):
    for chord in p4:
        main.set_notes(chord, M)
    main.set_rest(M)

filepath = pm.save_midi(mf, folder, filename)

#  mf.print_tracks()

subprocess.run(["timidity", "-c", "voices.cfg", filepath])
#  subprocess.run(["timidity", filepath, "-c", "voices.cfg", '-OF'])
