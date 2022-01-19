export class Bass extends Tone.FMSynth {

  constructor() {
    super({
      "harmonicity": 1,
      "modulationIndex": 3.5,
      "carrier": {
        "oscillator": {
          "type": "custom",
          "partials": [0, 1, 0, 2]
        },
        "envelope": {
          "attack": 0.08,
          "decay": 0.1,
          "sustain": 0,
          "release": 0.1
        },
      },
      "modulator": {
        "oscillator": {
          "type": "square"
        },
        "envelope": {
          "attack": 0.1,
          "decay": 0.2,
          "sustain": 0.3,
          "release": 0.01
        },
      }
    })
  }
}

//BASS
var bassEnvelope = new Tone.AmplitudeEnvelope({
  "attack" : 0.01,
  "decay" : 0.2,
  "sustain" : 0,
}).toMaster();

var bassFilter = new Tone.Filter({
  "frequency" : 600,
  "Q" : 8
});

export class Bass2 extends Tone.PulseOscillator{
  constructor() {
    super("A2", 0.4)
    this.chain(bassFilter, bassEnvelope);

  }
}
