'''
chord progressions
'''
import phimidi as pm
import phimidi.chords.chord_types as C

EBCsA = [
        (pm.N.E4, 4, C.major),
        (pm.N.B3, 4, C.major),
        (pm.N.Cs4, 4,C.minor),
        (pm.N.A3, 4, C.major),
        ]
EAGsABE = [
        (pm.N.E4, 2, C.major),
        (pm.N.A4, 2, C.major),
        (pm.N.Gs4, 4, C.minor_7),
        (pm.N.A3, 2, C.major),
        (pm.N.B3, 2, C.dominant_7),
        (pm.N.E3, 4, C.major),
        ]
p5 = [
        (pm.N.C3, 4, C.major),
        (pm.N.F3, 4, C.dominant_9),
        (pm.N.A3, 4, C.minor_7),
        (pm.N.G3, 4, C.dominant_11),
        (pm.N.A3, 4, C.minor_11),
        (pm.N.F3, 4, C.dominant_9),
        (pm.N.C3, 8, C.dominant_13),
        ]

