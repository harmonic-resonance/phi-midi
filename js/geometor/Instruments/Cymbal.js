// from Tonejs bembe example
// <a href="https://tonejs.github.io/docs/MetalSynth">Tone.MetalSynth</a>
// creates metallic, inharmonic sounds using 6
// <a href="https://tonejs.github.io/docs/FMOscillator">Tone.FMOscillators</a>
// with a tuning based on the TR-808 Cymbal.
export class Cymbal extends Tone.MetalSynth {
  constructor() {
    super({
      "harmonicity": 12,
      "resonance": 800,
      "modulationIndex": 20,
      "envelope": {
        "decay": 0.4,
      },
      "volume": -15
    })
  }
}
