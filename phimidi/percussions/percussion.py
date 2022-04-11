import phimidi as pm

class Percussion():

    """Docstring for Percussion. """

    def __init__(self, mf, inst_id, channel=9):
        """TODO: to be defined. """
        #  inst_id = pm.INSTRUMENTS.index(name)
        self.name = pm.P.PERCUSSIONS[inst_id]
        # instrument is the note on the drum channel
        self.instrument = inst_id
        self.channel = channel
        
        self.track = pm.set_new_track(mf, name=self.name)
        self.track.append(pm.Message('program_change', channel=channel, time=0))

        self.track_volume = pm.set_new_track(mf, name=f'{self.name}-volume')
        self.track_reverb = pm.set_new_track(mf, name=f'{self.name}-reverb')
        self.track_chorus = pm.set_new_track(mf, name=f'{self.name}-chorus')


    def set_rest(self, duration):
        duration = int(duration)
        self.track.append(pm.Message('note_off', note=0, channel=self.channel, velocity=127, time=duration))

    def set_hit(self, duration, velocity=64):
        duration = int(duration)
        self.track.append(pm.Message('note_on', note=self.instrument, channel=self.channel, velocity=velocity, time=0))
        self.track.append(pm.Message('note_off', note=self.instrument, channel=self.channel, velocity=127, time=duration))

    def set_volume(self, level, duration):
        duration = int(duration)
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=7, value=level, time=duration))

    def set_pan(self, level, duration):
        duration = int(duration)
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=10, value=level, time=duration))

    def set_balance(self, level, duration):
        duration = int(duration)
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=8, value=level, time=duration))

    def set_reverb(self, level, duration):
        duration = int(duration)
        self.track_reverb.append(pm.Message('control_change', channel=self.channel, control=91, value=level, time=duration))
        
    def set_chorus(self, level, duration):
        duration = int(duration)
        self.track_chorus.append(pm.Message('control_change', channel=self.channel, control=93, value=level, time=duration))
