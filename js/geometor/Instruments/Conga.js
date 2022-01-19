// from Tonejs bembe example
// <a href="https://tonejs.github.io/docs/MembraneSynth">Tone.MembraneSynth</a>
// makes kick and tom-like sounds using a frequency envelope which is triggered on notes attack.
export class Conga extends Tone.MembraneSynth {
  constructor() {
    super({
      "pitchDecay": 0.008,
      "octaves": 2,
      "envelope": {
        "attack": 0.0006,
        "decay": 0.5,
        "sustain": 0
      }
    })
  }
}
