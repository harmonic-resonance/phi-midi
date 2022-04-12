import phimidi.chords.chord_types as C

def get_chord_notes(root, chord_type):
    notes = []
    chord_intervals = C.CHORDS[chord_type]
    for interval in chord_intervals:
        notes.append(root + interval)
    return notes
    
