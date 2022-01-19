import * as Synths from '../Synths/_index.js'
import * as Effects from '../Effects/_index.js'

// tones from Brian Eno's Music for Airports
var airports = ["F4", "Ab4", "C5", "Db5", "Eb5", "F5", "Ab5"]

// var solfege = ["F4", "Ab4", "C5", "Db5", "Eb5", "F5", "Ab5"]
var pentatonic = ["C3", "G3", "D4", "A4", "E5", "C6"]
var fibTones = [55, 89, 144, 233, 377, 610]
var fibTones = [89, 144, 233, 377, 610, 987]

export function musicForFibonacci(Transport) {
  const synthPicker = document.querySelector("#synthPicker")
  var synthType = synthPicker.options[synthPicker.selectedIndex].value

  var F1 = 1
  var F2 = 1

  Transport.cancel(0)
  Transport.bpm.value = 120;

  // const synthType = "SquareSquare6"
  const synths = []

  airports.forEach( (note) => {

    var F3 =  F1 + F2
    var noteDuration = F1 + "m"
    var loopDuration = F3 + "m"

    synths[note] = Synths.getSynth(synthType);
    // synths[note].volume.value=-F2/2;
    synths[note].volume.value=-12;

    var reverb = new Tone.JCReverb(.9);
    // var delay = new Tone.FeedbackDelay(0);
    // var panner = new Tone.Panner(0);
    var panner = new Tone.AutoPanner({
			"frequency" : loopDuration,
			"depth" : 1
		}).start(noteDuration);

    synths[note].chain( reverb, panner, Tone.Master)

    var loop = new Tone.Loop(function(time){
      synths[note].triggerAttackRelease(note, noteDuration, time);
    }, loopDuration).start(noteDuration);

    F1 = F2
    F2 = F3

  } )


  Transport.stop(89)

  Transport.start()

}

export function musicForFibonacci2(Transport) {
  const synthPicker = document.querySelector("#synthPicker")
  var synthType = synthPicker.options[synthPicker.selectedIndex].value

  var F1 = 1
  var F2 = 1

  Transport.cancel(0)
  Transport.bpm.value = 360;

  // const synthType = "SquareSquare6"
  const synths = []

  fibTones.forEach( (note) => {

    var F3 =  F1 + F2
    var noteDuration = F1 + "m"
    var loopDuration = F3 + "m"

    synths[note] = Synths.getSynth(synthType);
    // synths[note].volume.value=-F2/2;
    synths[note].volume.value=-12;

    var reverb = new Tone.JCReverb(.9);
    // var delay = new Tone.FeedbackDelay(0);
    // var panner = new Tone.Panner(0);
    var panner = new Tone.AutoPanner({
			"frequency" : loopDuration,
			"depth" : 1
		}).start(noteDuration);

    synths[note].chain( reverb, panner, Tone.Master)

    var loop = new Tone.Loop(function(time){
      synths[note].triggerAttackRelease(note, noteDuration, time);
    }, loopDuration).start(noteDuration);

    F1 = F2
    F2 = F3

  } )


  Transport.stop(20)

  Transport.start()

}
