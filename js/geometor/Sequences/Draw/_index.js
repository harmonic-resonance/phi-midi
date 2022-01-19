import * as Synths from '../../Synths/_index.js'

export function setPoints(pointsSynth, start, root = "A4") {

  var fifth = Tone.Frequency(root).transpose(7).toNote()

  //TODO: set up Panner
  var part1 = new Tone.Part(function(time, note) {
    pointsSynth[0].triggerAttackRelease(note, "2n", time);
  }, [
    ["0:0", root],
  ])
  part1.start(start);

  var part2 = new Tone.Part(function(time, note) {
    pointsSynth[1].triggerAttackRelease(note, "2n", time);
  }, [
    ["0:0:1", fifth],
  ])
  part2.start(start);

}

export function setLine(pointsSynth, lineSynth, start, root) {

  setPoints(pointsSynth, start, root);

  var part = new Tone.Part(function(time, note) {
    lineSynth.triggerAttackRelease(note, "2n", time);
  }, [
    ["0:0", root],
  ]).start(start);

}

export function setCircle(pointsSynth, circleSynth, start, root) {

  setPoints(pointsSynth, start, root);

  var fifth = Tone.Frequency(root).transpose(-5).toNote()

  var part = new Tone.Part(function(time, note) {
    circleSynth.triggerAttackRelease(note, "4n", time);
  }, [
    ["0:0", root],
    ["0:1", fifth],
    ["0:2", root],
  ]).start(start);
}
