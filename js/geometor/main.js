import * as Instruments from './Instruments/_index.js'
import * as Seqs from './Sequences/_index.js'
import * as Recorder from './Recorder/_index.js'

const cymbal = new Instruments.Cymbal().toMaster();
Recorder.addInstrument(cymbal)

const conga  = new Instruments.Conga().toMaster();
Recorder.addInstrument(conga)

const bass   = new Instruments.Bass().toMaster();
Recorder.addInstrument(bass)

const piano  = new Instruments.Ping().toMaster();
Recorder.addInstrument(piano)

const ring  = new Instruments.Ring().toMaster();
Recorder.addInstrument(ring)


// when the Transport ends, stop the recorder
Tone.Transport.on("stop", () => {
  console.log("transport stop")
  Recorder.stop();
});

var started = false;
document.documentElement.addEventListener('mousedown', () => {

  if (started) return;
  started = true;

  Recorder.start();
  Seqs.Logo.play(Tone.Transport);

  Tone.Transport.start();
});
