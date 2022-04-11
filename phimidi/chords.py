'''utils for building chords
TODO: alternate voicings
'''
major = 'Major'
major_7 = 'Major7'
dominant_7 = 'Dominant7'
minor = 'Minor'
minor_7 = 'Minor7'
diminished = 'Diminished'
sus2 = 'Sus2'
sus4 = 'Sus4'

CHORDS = {
  'Major': [0, 4, 7],
  'Major7': [0, 4, 7, 11],
  'Dominant7': [0, 4, 7, 10],
  'Minor': [0, 3, 7],
  'Minor7': [0, 3, 7, 10],
  'Diminished': [0, 3, 6],
  'Sus2': [0, 2, 7],
  'Sus4': [0, 5, 7],
}
