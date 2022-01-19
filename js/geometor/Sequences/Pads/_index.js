
export const chords = {
  Major: [0, 4, 7],
  Major7: [0, 4, 7, 11],
  Dominant7: [0, 4, 7, 10],
  Minor: [0, 3, 7],
  Minor7: [0, 3, 7, 10],
  Diminished: [0, 3, 6],
  Sus2: [0, 2, 7],
  Sus4: [0, 5, 7],
}


export function padMaj(synth, start, root = "A4") {
  synth.volume.value=-12;
  var progression = Tone.Frequency(root).harmonize([0, 5, 7, 5])
  // console.dir(progression)

  var seq = new Tone.Sequence(function(time, note){
    var chord = Tone.Frequency(note).harmonize(chords.Dominant7);
    // console.dir(chord)
    synth.triggerAttackRelease(chord, "1m", time);

  }, progression, "1m").start(start);
  seq.loop = 1;
}
