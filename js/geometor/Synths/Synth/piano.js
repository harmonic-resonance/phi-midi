/**
 *  PIANO
 */
var piano = new Tone.PolySynth(4, Tone.Synth, {
  "volume" : -8,
  "oscillator" : {
    "partials" : [1, 2, 1],
  },
  "portamento" : 0.05
}).toMaster();

var cChord = ["C4", "E4", "G4", "B4"];
var dChord = ["D4", "F4", "A4", "C5"];
var gChord = ["B3", "D4", "E4", "A4"];

var pianoPart = new Tone.Part(function(time, chord){
  piano.triggerAttackRelease(chord, "8n", time);
}, [["0:0:2", cChord], ["0:1", cChord], ["0:1:3", dChord], ["0:2:2", cChord], ["0:3", cChord], ["0:3:2", gChord]]).start("2m");

pianoPart.loop = true;
pianoPart.loopEnd = "1m";
pianoPart.humanize = true;
