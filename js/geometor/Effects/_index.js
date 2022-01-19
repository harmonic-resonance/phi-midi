export function addFreeverb(synth){
  var freeverb = new Tone.Freeverb(.8, 100).toMaster();
  // freeverb.wet = .5;
  // freeverb.dampening.value = 1000;
  // routing synth through the reverb
  synth.connect(freeverb);
}
export function addReverb(synth) {
  var reverb = new Tone.JCReverb(.8).toMaster();
  var delay = new Tone.FeedbackDelay(0);
  synth.chain(delay, reverb);
}
