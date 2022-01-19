//BLEEP
var bleepEnvelope = new Tone.AmplitudeEnvelope({
  "attack" : 0.01,
  "decay" : 0.4,
  "sustain" : 0,
}).toMaster();

var bleep = new Tone.Oscillator("A4").connect(bleepEnvelope);
bleep.start();

var bleepLoop = new Tone.Loop(function(time){
   bleepEnvelope.triggerAttack(time);
}, "2n").start(0);
