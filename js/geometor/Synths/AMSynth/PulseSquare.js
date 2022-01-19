// Harmonics

export class PulseSquare extends Tone.AMSynth {

  constructor() {
    super(settings)
  }

}

const settings = {
  harmonicity: 2.88,
  detune: 0,
  oscillator: {
    frequency: 440,
    detune: 0,
    phase: 0,
    width: 0,
    volume: 0,
    mute: false,
    type: 'pulse'
  },
  envelope: {
    attack: 0.20958529411764706,
    decay: 1.9219607843137254,
    sustain: 0.08,
    release: 1.5132911764705883,
    attackCurve: 'exponential',
    decayCurve: 'linear',
    releaseCurve: 'exponential'
  },
  modulation: {
    type: 'square',
    frequency: 440,
    detune: 0,
    phase: 0,
    partialCount: 0,
    volume: 0,
    mute: false
  },
  modulationEnvelope: {
    attack: 0.01682843137254902,
    decay: 1.1665411764705882,
    sustain: 1,
    release: 2.151691176470588,
    attackCurve: 'linear',
    decayCurve: 'exponential',
    releaseCurve: 'exponential'
  },
  portamento: 0,
}
