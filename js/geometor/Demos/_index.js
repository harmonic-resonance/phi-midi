import * as Seqs from '../Sequences/_index.js'
import * as Airports from './Airports.js'
export {Airports}
import * as Download from './Download.js'
export {Download}

export function demo1(synth) {
  // Tone.Transport.position=0
  Tone.Transport.cancel(0)
  Tone.Transport.bpm.value = 120;


  Seqs.Draw.setPoints(synth, "0:0")
  Seqs.Draw.setPoints(synth, "0:1")
  Seqs.setPianoPart1(synth, "1:1")
  Seqs.setPianoPart2(synth, "2:1")
  Tone.Transport.stop("3:0")

  Tone.Transport.start(Tone.now())

}

export function demo2(synth) {
  // Tone.Transport.position=0
  Tone.Transport.cancel(0)
  Tone.Transport.bpm.value = 120;

  setPing1(synth, "0:1")
  setPing2(synth, "0:2")
  setPing2(synth, "0:3")
  setPing2(synth, "0:4")

  setPing1(synth, "1:1")
  setPing2(synth, "1:2")
  setPing2(synth, "1:3")
  setPing2(synth, "1:4")


  Tone.Transport.stop("2:0")

  Tone.Transport.start(Tone.now())

}

export function demo3(synth) {
  // Tone.Transport.position=0
  Tone.Transport.cancel(0)
  Tone.Transport.bpm.value = 120;

  Seqs.Pads.padMaj(synth, 0, "C5");

  Tone.Transport.stop("4:0")

  Tone.Transport.start(Tone.now())
}

function setPing1(synth, start) {

  var part1 = new Tone.Part(function(time, note) {
    synth.triggerAttackRelease(note, "8n", time);
  }, [
    ["0:0", "C6"],
  ]).start(start);
}
function setPing2(synth, start) {

  var part1 = new Tone.Part(function(time, note) {
    synth.triggerAttackRelease(note, "8n", time);
  }, [
    ["0:0", "C5"],
  ]).start(start);
}
