'''utils for building scales'''
from . import scale_types as S

def build_scale(root=48, scale_type=S.major, octaves=3):
    notes = [root]
    scale = S.SCALES[scale_type]
    for octave in range(octaves):
        jump = 0
        for interval in scale:
            jump += interval
            note = (octave * 12) + root + jump
            notes.append(note)
    return notes

