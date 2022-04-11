import phimidi as pm

class Voice():

    """Docstring for Voice. """

    def __init__(self, mf, voice_name):
        """TODO: to be defined. """
        #  inst_id = pm.INSTRUMENTS.index(name)
        voice_dict = pm.V.VOICES[voice_name]
        self.name = voice_name
        self.instrument = voice_dict['program']
        self.channel = voice_dict['channel']
        
        self.track = pm.set_new_track(mf, name=voice_name)
        
        self.track.append(pm.Message(
            'control_change', 
            control =  0, 
            value = voice_dict['bank'], 
            channel = self.channel,
            time = 0
        ))
        self.track.append(pm.Message(
            'control_change', 
            control = 32, 
            value = voice_dict['subbank'], 
            channel = self.channel,
            time = 0
        ))
        self.track.append(pm.Message(
            'program_change', 
            program = voice_dict['program'],
            channel = self.channel,
            time = 1))

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

    def add_voice_track(mf, name='Mixed Choir'):
        track = pm.set_new_track(mf, name=name)
        v = VOICES[name]
        
        track.append(pm.Message(
            'control_change', 
            control =  0, 
            value = v['bank'], 
            channel = v['channel'], 
            time = 0
        ))
        track.append(pm.Message(
            'control_change', 
            control = 32, 
            value = v['subbank'], 
            channel = v['channel'], 
            time = 0
        ))
        track.append(pm.Message(
            'program_change', 
            program = v['program'],
            channel = v['channel'], 
            time = 1))
        return track

    def add_voice_note(track, note, velocity=64, duration=1920):
        v = VOICES[track.name]
        pm.set_note(track, note, channel=v['channel'], velocity=64, duration=duration)

    def add_voice_chord(track, root, chord='Major', velocity=64, duration=1920):
        v = VOICES[track.name]
        # pm.set_note(track, note, channel=v['channel'], duration=1920*2)
        pm.set_chord(track, root=root, chord=chord, channel=v['channel'], velocity=64, duration=duration)
     
