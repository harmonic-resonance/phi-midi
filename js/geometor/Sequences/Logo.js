import * as Seqs from './_index.js'
import * as Instruments from '../Instruments/_index.js'
import * as Synths from '../Synths/_index.js'




export function play(Transport) {

  // const bass   = new Instruments.Conga().toMaster();
  const piano  = new Instruments.Ping().toMaster();
  const ring  = new Instruments.Ring().toMaster();

  // const cymbal  = new Instruments.Cymbal().toMaster();
  // cymbal.volume.value = -24;
  const pointsSynths = [];
  for (var i = 0; i < 4; i++) {
    pointsSynths[i] = Synths.getSynth("AMSine2").toMaster();
  }
  const lineSynth = Synths.getSynth("ElectricCello").toMaster();
  const circleSynth = Synths.getSynth("ElectricCello").toMaster();


  Transport.bpm.value = 240;
  // Tone.Transport.cancel(0);

  // Seqs.Rhythms.setCymbalPart2(cymbal, "0:0");
  // setKickPart();
  Seqs.setBass(piano, "0:2:0");
  // line
  // Seqs.Draw.setPoints(pointsSynths, "0:3:0", "C5");
  Seqs.Draw.setLine(pointsSynths, lineSynth, "0:3:0", "C4");
  // vesica
  Seqs.Draw.setCircle(pointsSynths, circleSynth, "1:1:0", "G4");
  // fade
  Seqs.setBass(piano, "1:4:0");
  // 4 lines
  Seqs.Draw.setLine(pointsSynths, lineSynth, "2:1:0", "F5");
  // triangle
  Seqs.Draw.setCircle(pointsSynths, circleSynth, "2:3:0", "C5");
  // 2 medians
  Seqs.Draw.setLine(pointsSynths, lineSynth, "3:2:0", "F5");
  // main circle
  Seqs.Draw.setCircle(pointsSynths, circleSynth, "3:4:0", "G5");
  // fill
  Seqs.setBass(piano, "4:4:0");
  // first golden
  Seqs.Draw.setLine(pointsSynths, lineSynth, "5:2:0", "C4");
  // second golden
  Seqs.Draw.setLine(pointsSynths, lineSynth, "5:4:0", "C5");

  // console.log(Transport.seconds)
  //fill
  Seqs.setBass(piano, "7:1:0");

  Transport.stop("9:0:0")

  Transport.start();

}
