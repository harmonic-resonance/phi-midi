//BASS
var bassEnvelope = new Tone.AmplitudeEnvelope({
  "attack" : 0.01,
  "decay" : 0.2,
  "sustain" : 0,
}).toMaster();

var bassFilter = new Tone.Filter({
  "frequency" : 600,
  "Q" : 8
});

var bass = new Tone.PulseOscillator("A2", 0.4).chain(bassFilter, bassEnvelope);
bass.start();

var bassPart = new Tone.Part(function(time, note){
  bass.frequency.setValueAtTime(note, time);
  bassEnvelope.triggerAttack(time);
}, [["0:0", "A1"],
  ["0:2", "G1"],
  ["0:2:2", "C2"],
  ["0:3:2", "A1"]]).start(0);
