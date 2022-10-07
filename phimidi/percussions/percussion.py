import phimidi as pm
from ..instruments import Instrument

class Percussion(Instrument):

    """Docstring for Percussion. """

    def __init__(self, mf, inst_id, channel=9):
        """TODO: to be defined. """
        #  inst_id = pm.INSTRUMENTS.index(name)
        self.name = pm.P.PERCUSSIONS[inst_id]
        # instrument is the note on the drum channel
        self.instrument = inst_id
        # default midi drum channel is 10 (9 index)
        self.channel = channel

        self.track = mf.add_track(name=self.name)
        self.track.append(pm.Message('program_change', channel=channel, time=0))

        # TODO:  set volume and pan for percussion at part level
        #  self.track_volume = mf.add_track(name=f'{self.name}-volume')
        #  self.track_pan = mf.add_track(name=f'{self.name}-pan')

    def set_hit(self, duration, velocity=64):
        duration = int(duration)
        self.track.append(pm.Message('note_on', note=self.instrument, channel=self.channel, velocity=velocity, time=0))
        self.track.append(pm.Message('note_off', note=self.instrument, channel=self.channel, velocity=127, time=duration))

    def set_hits(self, duration, divisions, velocity=64):
        duration = int(duration/divisions)
        for _ in range(divisions):
            self.track.append(pm.Message('note_on', note=self.instrument, channel=self.channel, velocity=velocity, time=0))
            self.track.append(pm.Message('note_off', note=self.instrument, channel=self.channel, velocity=127, time=duration))

    def add_pattern(self, pattern: str, b: int, velocity_mod: int=0):
        """TODO: Docstring for add_pattern.
        :pattern: str with one character for rest or hit
        :b: int duration for beat
        :velocity_mod: adjust overall velocity for pattern +/-

        """
        for p in pattern:
            if p == '_':
                self.set_rest(b)
            elif p == '-':
                # TODO: dash to extend duration of previous hit
                self.set_rest(b)
            else:
                v = int(p) * 12 + velocity_mod
                self.set_hit(b, velocity=v)

