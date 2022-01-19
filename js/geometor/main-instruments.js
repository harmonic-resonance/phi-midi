import * as Instruments from './Instruments/_index.js'
import * as Seqs from './Sequences/_index.js'
import * as Effects from './Effects/_index.js'
import * as Synths from './Synths/_index.js'
import * as Demos from './Demos/_index.js'
import * as Download from './Recorder/download.js'

//bind the interface
const picker = document.querySelector("#synthPicker")
const poly = document.querySelector("#poly")

function addSynthListToPicker(value, key, map) {
  var el = document.createElement("option");
  el.textContent = key;
  el.value = key;
  picker.appendChild(el);
}

Synths.synthList.forEach(addSynthListToPicker);

picker.onchange = setSynth;
poly.onchange = setSynth;

var synth;
setSynth();
// Effects.addFreeverb(synth);

function setSynth() {
  var pick = picker.options[picker.selectedIndex].value
  console.log("set: " + pick)

  if (poly.checked) {
    synth = Synths.getPolySynth(pick);

    document.querySelector("tone-piano").bind(synth);
    // document.querySelector("tone-am-synth").unbind();
  } else {
    synth = Synths.getSynth(pick);

    document.querySelector("tone-piano").bind(synth);
    document.querySelector("tone-am-synth").bind(synth);
  }
  synth.toMaster();
}

document.querySelector("#demo1").onclick = demo1;
document.querySelector("#demo2").onclick = demo2;
document.querySelector("#logo").onclick = logo;
document.querySelector("#fib1").onclick = fib1;
document.querySelector("#fib2").onclick = fib2;

function logo() {
  console.log("logo")
  Seqs.Logo.play(Tone.Transport)
}
function demo1() {
  console.log("demo1")
  Demos.demo1(synth)
}

function demo2() {
  console.log("demo2")
  Demos.demo2(synth)
}

function fib1() {
  console.log("fib1")
  // var pick = picker.options[picker.selectedIndex].value

  Demos.Download.musicForFibonacci(Tone.Transport)

}
function fib2() {
  console.log("fib2")
  // var pick = picker.options[picker.selectedIndex].value

  Demos.Download.musicForFibonacci2(Tone.Transport)
}

function generateAudioOffline() {

  //the play() function receives the Offline Transport as a parameter

  // return Tone.Offline(Seqs.Logo.play, 10);
  // return Tone.Offline(Demos.Download.musicForFibonacci, 89);
  return Tone.Offline(Seqs.Logo.play, 10);
}

Tone.Transport.on("stop", () => {
  console.log("transport stop")
  Tone.context.close();
});

Tone.Transport.on("start", () => {
  console.log("transport start")
});

//play the buffer with a Tone.Player when it's been generated
var player = new Tone.Player().toMaster();
document.querySelector("tone-player").bind(player);

//bind the interface
document.querySelector("tone-button").addEventListener("click", e => {
  //button
  e.target.setAttribute("label", "Rendering...");
  e.target.setAttribute("disabled", "");

  var buffer = generateAudioOffline().then(buffer => {

    document.querySelector("tone-button").setAttribute("label", "Rendered");
    player.buffer = buffer;
    document.querySelector("tone-play-toggle").removeAttribute("disabled");

    Download.toWav(buffer, buffer.length, "logo");

    // let blob = new Blob([buffer], { type: 'audio/webm;codecs=opus' });
    // const audio = document.querySelector('audio');
    // audio.src = URL.createObjectURL(buffer);

  });

});
document.querySelector("tone-play-toggle").bind(player);
document.querySelector("tone-oscilloscope").bind(player);
document.querySelector("tone-fft").bind(player);

/////

// document.querySelector("tone-play-toggle").bind(Tone.Transport);
// document.querySelector("tone-metal-synth").bind(cymbal);
// document.querySelector("tone-membrane-synth").bind(conga);
// document.querySelector("tone-fm-synth").bind(bass);
