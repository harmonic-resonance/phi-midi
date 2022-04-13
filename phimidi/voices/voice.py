import phimidi as pm
from phimidi.instruments import Instrument

class Voice(Instrument):

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
        self.track_pan = pm.set_new_track(mf, name=f'{self.name}-pan')
        #  self.track_reverb = pm.set_new_track(mf, name=f'{self.name}-reverb')
        #  self.track_chorus = pm.set_new_track(mf, name=f'{self.name}-chorus')


