#  from mido import *
from mido import MidiFile, Message, MetaMessage, bpm2tempo, second2tick
import phimidi.notes as N
from phimidi.scales import *
from phimidi.chords import *
from phimidi.instruments import *
from phimidi.voices import *
from phimidi.percussions import *
from phimidi.arps import *


def new_midi(title='', tempo=500000):
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

def set_note(track, note=60, channel=0, velocity=64, duration=480):
    duration = int(duration)
    track.append(Message('note_on', note=note, channel=channel, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, channel=channel, velocity=127, time=duration))
    
def set_note_on(track, note=60, channel=0, velocity=64, duration=480):
    duration = int(duration)
    track.append(Message('note_on', note=note, channel=channel, velocity=velocity, time=0))
    track.append(Message('note_on', note=0, channel=channel, velocity=velocity, time=0))
    track.append(Message('note_off', note=0, channel=channel, velocity=127, time=duration))
    
def set_chord(track, root=60, chord_type=C.major, channel=0, velocity=64, duration=480):
    duration = int(duration)
    chord = pm.C.CHORDS[chord_type]
    for offset in chord:
        track.append(Message('note_on', note=root+offset, channel=channel, velocity=velocity, time=0))
    for offset in chord:
        if offset == 0:
            time = duration
        else:
            time = 0
        track.append(Message('note_off', note=root+offset, channel=channel, velocity=127, time=time))
    
def save_midi(mf, folder, filename):
    import os
    sessions = os.path.expanduser('~') + '/Sessions'
    out = f'{sessions}/{folder}/'
    os.makedirs(out, exist_ok=True)
    filepath = out + filename
    mf.save(filepath)
    print(f'    * {filepath}')
    return filepath

