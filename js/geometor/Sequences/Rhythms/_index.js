//https://teropa.info/blog/2016/07/28/javascript-systems-music.html#the-notes-and-intervals-in-music-for-airports


export function setCymbalPart(synth, start) {

  var part = new Tone.Sequence(function(time, freq) {
    synth.frequency.setValueAtTime(freq, time, Math.random() * 0.5 + 0.5);
    synth.triggerAttack(time);
  }, [
    [300, null, 200],
    [null, 200, 200],
    [null, 200, null],
    [200, null, 200]
  ], "4n").start(start);

  return part;

}

export function setCymbalPart2(synth, start) {

  var part = new Tone.Sequence(function(time, freq) {
    synth.frequency.setValueAtTime(freq, time, Math.random() * 0.5 + 0.5);
    synth.triggerAttack(time);
  }, [
    [300, 200, ]
  ], "8n").start(0);

  return part;

}

export function setCongaPart(synth, start) {

  var part = new Tone.Sequence(function(time, pitch) {
    synth.triggerAttack(pitch, time, Math.random() * 0.5 + 0.5);
  }, ["G2", "D3", "D3", "D3"], "4n").start(start);

  return part;


}

export function setKickPart(synth, start) {

  var part = new Tone.Sequence(function(time, pitch) {
    synth.triggerAttack(pitch, time, Math.random() * 0.5 + 0.5);
  }, ["G2"], "4n").start(start);

  return part;


}
