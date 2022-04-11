import phimidi as pm

class Instrument():

    """Docstring for Instrument. """

    def __init__(self, mf, inst_id, channel):
        """TODO: to be defined. """
        #  inst_id = pm.INSTRUMENTS.index(name)
        self.name = pm.I.INSTRUMENTS[inst_id]
        self.instrument = inst_id
        self.channel = channel
        
        self.track = pm.set_new_track(mf, name=self.name)
        self.track.append(pm.Message('program_change', channel=channel, program=inst_id, time=0))

        self.track_volume = pm.set_new_track(mf, name=f'{self.name}-volume')
        self.track_reverb = pm.set_new_track(mf, name=f'{self.name}-reverb')
        self.track_chorus = pm.set_new_track(mf, name=f'{self.name}-chorus')


    def set_rest(self, duration):
        self.track.append(pm.Message('note_off', note=0, channel=self.channel, velocity=127, time=duration))

    def set_note(self, note, duration, velocity=64):
        self.track.append(pm.Message('note_on', note=note, channel=self.channel, velocity=velocity, time=0))
        self.track.append(pm.Message('note_off', note=note, channel=self.channel, velocity=127, time=duration))

    def set_chord(self, root, duration, chord_type=pm.C.major, velocity=64):
        chord = pm.C.CHORDS[chord_type]
        for offset in chord:
            self.track.append(pm.Message('note_on', note=root+offset, channel=self.channel, velocity=velocity, time=0))
        for offset in chord:
            if offset == 0:
                time = duration
            else:
                time = 0
            self.track.append(pm.Message('note_off', note=root+offset, channel=self.channel, velocity=127, time=time))

    def set_volume(self, level, duration):
        self.track_volume.append(pm.Message('control_change', channel=self.channel, control=7, value=level, time=duration))

    def set_reverb(self, level, duration):
        self.track_reverb.append(pm.Message('control_change', channel=self.channel, control=91, value=level, time=duration))
        
    def set_chorus(self, level, duration):
        self.track_chorus.append(pm.Message('control_change', channel=self.channel, control=93, value=level, time=duration))
