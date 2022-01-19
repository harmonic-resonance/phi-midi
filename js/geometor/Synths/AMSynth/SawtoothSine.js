// FatSawtooth AMSynth

export class SawtoothSine extends Tone.AMSynth {

  constructor() {
    super(settings)
  }

}

const settings = {
  harmonicity: 3.51,
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
    attack: 0.01682843137254902,
    decay: 0.2,
    sustain: 0.3,
    release: 0.3,
    attackCurve: 'linear',
    decayCurve: 'exponential',
    releaseCurve: 'exponential'
  },
  modulation: {
    type: 'sine',
    frequency: 440,
    detune: 0,
    phase: 0,
    partialCount: 0,
    volume: 0,
    mute: false
  },
  modulationEnvelope: {
    attack: 0.6661147058823529,
    decay: 1.1665411764705882,
    sustain: 1,
    release: 2.151691176470588,
    attackCurve: 'linear',
    decayCurve: 'exponential',
    releaseCurve: 'exponential'
  },
  portamento: 0,
}
