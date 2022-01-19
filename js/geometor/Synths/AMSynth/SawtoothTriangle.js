// FatSawtooth AMSynth

export class SawtoothTriangle extends Tone.AMSynth {

  constructor() {
    super(settings)
  }

}

const settings = {
  harmonicity: 2.355,
  detune: 0,
  oscillator: {
    type: 'sawtooth',
    frequency: 440,
    detune: 0,
    phase: 0,
    partialCount: 0,
    volume: 0,
    mute: false
  },
  envelope: {
    attack: 0.19729411764705884,
    decay: 1.1072313725490197,
    sustain: 0.3,
    release: 2.8358588235294118,
    attackCurve: 'linear',
    decayCurve: 'exponential',
    releaseCurve: 'exponential'
  },
  modulation: {
    type: 'triangle',
    frequency: 440,
    detune: 0,
    phase: 0,
    partialCount: 0,
    volume: 0,
    mute: false
  },
  modulationEnvelope: {
    attack: 0.09584313725490196,
    decay: 1.1665411764705882,
    sustain: 1,
    release: 2.151691176470588,
    attackCurve: 'linear',
    decayCurve: 'exponential',
    releaseCurve: 'exponential'
  },
  portamento: 0,
}
