import * as AMSynth from './AMSynth/_index.js'
export {AMSynth}
// export * as AMSynth from './AMSynth/_index.js'

import * as FMSynth from './FMSynth/_index.js'
export {FMSynth}
import * as MembraneSynth from './MembraneSynth/_index.js'
export {MembraneSynth}
import * as MetalSynth from './MetalSynth/_index.js'
export {MetalSynth}
import * as MonoSynth from './MonoSynth/_index.js'
export {MonoSynth}
import * as NoiseSynth from './NoiseSynth/_index.js'
export {NoiseSynth}
import * as Synth from './Synth/_index.js'
export {Synth}

export const synthList = new Map([
  ['AMSine2', AMSynth.AMSine2],
  ['FatSawtoothSquare', AMSynth.FatSawtoothSquare],
  ['PulseSquare', AMSynth.PulseSquare],
  ['SawtoothSine', AMSynth.SawtoothSine],
  ['SawtoothTriangle', AMSynth.SawtoothTriangle],
  ['SquareSquare6', AMSynth.SquareSquare6],
  ['ElectricCello', FMSynth.ElectricCello],
  ['Kalimba', FMSynth.Kalimba],
]);

export function getSynth(name) {
  return new ( synthList.get(name) )()
}

export function getPolySynth(name) {
  return new Tone.PolySynth(8, synthList.get(name) )
}
// console.log(bar);
