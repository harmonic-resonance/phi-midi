NOTES = {
    'C4': 60,
}

#  NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
#  OCTAVES = list(range(11))
#  NOTES_IN_OCTAVE = len(NOTES)

#  errors = {
    #  'program': 'Bad input, please refer this spec-\n'
               #  'http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/program_change.htm',
    #  'notes': 'Bad input, please refer this spec-\n'
             #  'http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm'
#  }


#  def instrument_to_program(instrument: str) -> int:
    #  assert instrument in INSTRUMENTS, errors['program']
    #  return INSTRUMENTS.index(instrument) + 1


#  def program_to_instrument(program: int) ->  str:
    #  assert 1 <= program <= 128, errors['program']
    #  return INSTRUMENTS[program - 1]


#  def number_to_note(number: int) -> tuple:
    #  octave = number // NOTES_IN_OCTAVE
    #  assert octave in OCTAVES, errors['notes']
    #  assert 0 <= number <= 127, errors['notes']
    #  note = NOTES[number % NOTES_IN_OCTAVE]

    #  return note, octave


#  def note_to_number(note: str, octave: int) -> int:
    #  assert note in NOTES, errors['notes']
    #  assert octave in OCTAVES, errors['notes']

    #  note = NOTES.index(note)
    #  note += (NOTES_IN_OCTAVE * octave)

    #  assert 0 <= note <= 127, errors['notes']

    #  return note
