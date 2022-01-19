export class Piano extends Tone.Synth {

  constructor() {

    super({
      "oscillator": {
        "type": "fmsine4",
        "modulationType": "square"
      }
    })
  }
}

export class Ping extends Tone.Synth {

  constructor() {

    super({
      oscillator: {
        type: "sine"
      },
      envelope: {
        attack: 0.01,
        decay: 1.2,
        sustain: 0,
        release: 1.2
      }
    })
  }
}

export class Ring extends Tone.FMSynth {

  constructor() {

    super({
      harmonicity: 3,
      modulationIndex: 10,
      detune: 0,
      oscillator: {
        type: "sine"
      },
      envelope: {
        attack: 0.1,
        decay: 0.01,
        sustain: 1,
        release: 0.8
      },
      modulation: {
        type: "square"
      },
      modulationEnvelope: {
        attack: 0.2,
        decay: 0,
        sustain: 1,
        release: 0.5
      }
    })
  }
}


export class PolyPing extends Tone.PolySynth {
  constructor() {
    super(6, Ping)
  }
}
