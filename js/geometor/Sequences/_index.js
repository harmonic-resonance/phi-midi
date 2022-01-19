//instruments must be connected to the stream dest for recording.
import * as Rhythms from './Rhythms/_index.js'
export {Rhythms}
import * as Pads from './Pads/_index.js'
export {Pads}
import * as Draw from './Draw/_index.js'
export {Draw}
import * as Logo from './Logo.js'
export {Logo}


export function setBass(synth, start) {
  var part = new Tone.Part(function(time, note) {
    synth.triggerAttackRelease(note, "1n", time);
  }, [
    ["0:0", "C3"],
  ]).start(start);
}



export function setPianoPart1(synth, start) {
  var part = new Tone.Part(function(time, note) {
    synth.triggerAttackRelease(note, "4n", time);
  }, [
    ["0:0", "C2"],
    ["0:1", "E2"],
    ["0:2", "C2"],
    ["0:3", "G2"],
  ]).start(start);

}

export function setPianoPart2(synth, start) {
  var part = new Tone.Part(function(time, note) {
    synth.triggerAttackRelease(note, "8n", time);
  }, [
    ["0:0", "C3"],
    ["0:1", "E3"],
    ["0:2", "C3"],
    ["0:3", "G3"],
  ]).start(start);

  return part;

}
