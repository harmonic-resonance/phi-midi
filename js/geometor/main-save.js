import * as Instruments from './instruments/_index.js'
import * as Seqs from './Sequences/_index.js'
import * as WavCreator from './Recorder/audioBufferToWav.js'




// when the Transport ends, stop the recorder
Tone.Transport.on("stop", () => {
  console.log("transport stop")
});

var started = false;
document.documentElement.addEventListener('mousedown', () => {

  var buffer = generateAudioOffline().then(buffer => {
    // document.querySelector("tone-button").setAttribute("label", "Rendered");
    // player.buffer = buffer;
    // document.querySelector("tone-play-toggle").removeAttribute("disabled");
    var wav = WavCreator.audioBufferToWav(buffer, buffer.length);
    var new_file = URL.createObjectURL(wav);

    var download_link = document.getElementById("download_link");
    download_link.href = new_file;
    // var name = generateFileName("test");
    var name = "test" + ".wav";
    download_link.download = name;
    download_link.innerHTML = name;
    // let blob = new Blob([buffer], { type: 'audio/webm;codecs=opus' });
    // const audio = document.querySelector('audio');
    // audio.src = URL.createObjectURL(buffer);

  });


});

function generateAudioOffline() {
  //the makeMusic function receives the Offline Transport as a parameter
  return Tone.Offline(makeMusic, 3);
}

function makeMusic(Transport) {
  const piano = new Instruments.Ping().toMaster();

  Transport.bpm.value = 120;

  Seqs.setPianoPart2(piano, "0:0");

  Transport.start();

}
