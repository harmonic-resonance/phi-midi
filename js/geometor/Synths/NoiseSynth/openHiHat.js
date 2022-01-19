//filtering the hi-hats a bit
//to make them sound nicer
var lowPass = new Tone.Filter({
  "frequency" : 14000,
}).toMaster();

//we can make our own hi hats with
//the noise synth and a sharp filter envelope
var openHiHat = new Tone.NoiseSynth({
  "volume" : -10,
  "filter" : {
    "Q" : 1
  },
  "envelope" : {
    "attack" : 0.01,
    "decay" : 0.3
  },
  "filterEnvelope" : {
    "attack" : 0.01,
    "decay" : 0.03,
    "baseFrequency" : 4000,
    "octaves" : -2.5,
    "exponent" : 4,
  }
}).connect(lowPass);

var openHiHatPart = new Tone.Part(function(time){
  openHiHat.triggerAttack(time);
}, [{ "8n" : 2 }, { "8n" : 6 }]).start(0);
