'''
chord progressions
includes patterns from:
https://www.learnjazzstandards.com/blog/learning-jazz/jazz-theory/3-important-jazz-chord-progressions-need-master/
'''
import phimidi as pm
#  import phimidi.chords.chord_types as C
from . import chord_types as C

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


EBCsA = [
        (pm.N.E4, 4, C.major),
        (pm.N.B3, 4, C.major),
        (pm.N.Cs4, 4, C.minor),
        (pm.N.A3, 4, C.major),
        ]


def I_V_vis_IV(root):
    I = pm.get_chord_notes(0 + root, C.major)
    V = pm.get_chord_notes(7 + root, C.dominant_7)
    vis = pm.get_chord_notes(10 + root, C.minor)
    IV = pm.get_chord_notes(5 + root, C.dominant_7)

    return [I, V, vis, IV]


def ii_V_i(root):
    ii = pm.get_chord_notes(2 + root, C.minor_7)
    V = pm.get_chord_notes(7 + root, C.dominant_7)
    i = pm.get_chord_notes(0 + root, C.major_7)

    return [ii, V, i]


def build_progression(key, chords: list):
    """TODO: Docstring for build_progression.

    :key: TODO
    :chords: TODO
    :returns: TODO

    """
    progression = []
    for name, (note, chord_type) in chords.items():
        notes = pm.get_chord_notes(key[note], chord_type)
        progression.append((name, notes))

    return progression


def I_vi_ii_V(root: int):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = {
            'I': (1, C.major_7),
            'vi': (6, C.minor_7),
            'ii': (2, C.minor_7),
            'V': (5, C.dominant_7)
            }

    return build_progression(key, chords)


def i_vi_ii_V(root: int):
    key = pm.Scale(root, scale_type=pm.S.major)
    chords = {
            'i': (1, C.minor_7),
            'vi': (6, C.minor_7),
            'ii': (2, C.minor_7),
            'V': (5, C.dominant_7)
            }

    return build_progression(key, chords)

#  p5 = [
        #  (pm.N.C3, 4, C.major),
        #  (pm.N.F3, 4, C.dominant_9),
        #  (pm.N.A3, 4, C.minor_7),
        #  (pm.N.G3, 4, C.dominant_11),
        #  (pm.N.A3, 4, C.minor_11),
        #  (pm.N.F3, 4, C.dominant_9),
        #  (pm.N.C3, 8, C.dominant_13),
        #  ]

def p5(root):
    chords = [
            pm.get_chord_notes(0 + root, C.major_7),
            pm.get_chord_notes(5 + root, C.dominant_9),
            pm.get_chord_notes(9 + root, C.minor_7),
            pm.get_chord_notes(7 + root, C.dominant_11),
            pm.get_chord_notes(9 + root, C.minor_11),
            pm.get_chord_notes(0 + root + 12, C.major_7),
            ]

    return chords

