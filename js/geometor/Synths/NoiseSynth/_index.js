export {gravel} from './gravel.js'
export {slap} from './slap.js'
export {swoosh} from './swoosh.js'
export {train} from './train.js'

export const snare = new Tone.NoiseSynth({
  "volume" : -5,
  "envelope" : {
    "attack" : 0.001,
    "decay" : 0.2,
    "sustain" : 0
  },
  "filterEnvelope" : {
    "attack" : 0.001,
    "decay" : 0.1,
    "sustain" : 0
  }
})
