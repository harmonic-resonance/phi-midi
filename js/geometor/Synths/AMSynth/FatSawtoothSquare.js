// FatSawtooth AMSynth

const settings = {
  "harmonicity" : 2.5,
  "oscillator" : {
    "type" : "fatsawtooth"
  },
  "envelope" : {
    "attack" : 0.1,
    "decay" : 0.2,
    "sustain" : 0.2,
    "release" : 0.3
  },
  "modulation" : {
    "type" : "square"
  },
  "modulationEnvelope" : {
    "attack" : 0.5,
    "decay" : 0.01
  }
}

export class FatSawtoothSquare extends Tone.AMSynth {

  constructor() {
    super(settings)
  }

}
