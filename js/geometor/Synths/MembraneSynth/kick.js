var kick = new Tone.MembraneSynth({
  "envelope" : {
    "sustain" : 0,
    "attack" : 0.02,
    "decay" : 0.8
  },
  "octaves" : 10
})

// var kickPart = new Tone.Loop(function(time){
//   kick.triggerAttackRelease("C2", "8n", time);
// }, "2n").start(0);
