'''
arpeggio functions
'''

def add_arp_up(instrument, notes, length):
    beat = length / len(notes)
    for note in notes:
        instrument.set_note(note, beat)

def add_arp_down(instrument, notes, length):
    beat = length / len(notes)
    for note in reversed(notes):
        instrument.set_note(note, beat)


