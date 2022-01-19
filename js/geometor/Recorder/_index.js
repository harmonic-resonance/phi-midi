const audio = document.querySelector('audio');
export const dest = Tone.context.createMediaStreamDestination();


const chunks = [];

const recorder = new MediaRecorder(dest.stream);

export function start(){
  recorder.start();
}
export function stop(){
  recorder.stop();
}

export function addInstrument(instrument) {
  instrument.connect(dest)
}
recorder.ondataavailable = evt => {
  console.log("recorder on data")
  chunks.push(evt.data);
}

recorder.onstop = evt => {
  console.log("recorder stop")
  console.dir(chunks)

  let blob = new Blob(chunks, { type: 'audio/webm;codecs=opus' });
  audio.src = URL.createObjectURL(blob);
};
