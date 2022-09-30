#  from mido import *
from mido import MidiFile, Message, MetaMessage, bpm2tempo, second2tick, tick2second
#  import .notes as N
from . import notes as N
from .scales import *
from .chords import *
from .instruments import *
from .voices import *
from .percussions import *
from .arps import *


class Session(MidiFile):

    """Docstring for Session. """
    free_channels = list(range(16))
    perc_channel = free_channels.remove(9)

    def __init__(self, title, tempo=500000):
        """TODO: to be defined.

        :title: TODO
        :tempo: TODO

        """
        #  MidiFile.__init__(self)
        super().__init__()

        self.title = title
        self.tempo = tempo
        
        track = self.add_track(name='meta')
        if title:
            track.append(MetaMessage('text', text=title, time=0))
        track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

    def save(self, folder, filename):
        import os
        sessions = os.path.expanduser('~') + '/Sessions'
        out = f'{sessions}/{folder}/'
        os.makedirs(out, exist_ok=True)
        filepath = out + filename
        super().save(filepath)
        print(f'    * {filepath}')
        return filepath

    def add_instrument(self, instrument_type: I) -> Instrument:
        """add instrument to session
        set to next available channel

        :instrument_type: TODO
        :returns: TODO

        """
        return Instrument(self, instrument_type, channel)

    def add_piano(self, channel):
        return Instrument(mf, I.acoustic_grand_piano, channel)

    def make_vibes(mf, channel):
        return Instrument(mf, I.vibraphone, channel)

    def make_bass(mf, channel):
        return Instrument(mf, I.acoustic_bass, channel)

    def make_horns(mf, channel):
        return Instrument(mf, I.brass_section, channel)

    def make_strings(mf, channel):
        return Instrument(mf, I.string_ensemble_1, channel)


def new_midi(title='', tempo=500000) -> MidiFile:
    '''sets up a mido midi file with initial meta track'''
    mf = MidiFile()

    track = mf.add_track(name='meta')
    if title:
        track.append(MetaMessage('text', text=title, time=0))
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
    return mf

def set_new_track(mf, name='', instrument=''):
    track = mf.add_track(name=name)
    # if instrument:
        # track.append(MetaMessage('text', text='TITLE', time=0))
    return track


    
def save_midi(mf, folder, filename):
    import os
    sessions = os.path.expanduser('~') + '/Sessions'
    out = f'{sessions}/{folder}/'
    os.makedirs(out, exist_ok=True)
    filepath = out + filename
    mf.save(filepath)
    print(f'    * {filepath}')
    return filepath

