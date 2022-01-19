/*
 BASS
 */
var bass = new Tone.MonoSynth({
  "volume" : -10,
  "envelope" : {
    "attack" : 0.1,
    "decay" : 0.3,
    "release" : 2,
  },
  "filterEnvelope" : {
    "attack" : 0.001,
    "decay" : 0.01,
    "sustain" : 0.5,
    "baseFrequency" : 200,
    "octaves" : 2.6
  }
}).toMaster();

var bassPart = new Tone.Sequence(function(time, note){
  bass.triggerAttackRelease(note, "16n", time);
}, ["C2", ["C3", ["C3", "D2"]], "E2", ["D2", "A1"]]).start(0);

bassPart.probability = 0.9;
