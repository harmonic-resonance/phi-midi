from mido import Message, MidiFile, MidiTrack, MetaMessage
from phimidi.scales import *
from phimidi.chords import *
from phimidi.voices import *
from phimidi.percussion import *
from phimidi.instruments import *
from phimidi.notes import *


def new_midi(title=''):
    '''sets up a mido midi file with initial meta track'''
    mf = MidiFile()

    track = mf.add_track(name='meta')
    if title:
        track.append(MetaMessage('text', text=title, time=0))
    return mf

def set_new_track(mf, name='', instrument=''):
    track = mf.add_track(name=name)
    # if instrument:
        # track.append(MetaMessage('text', text='TITLE', time=0))
    return track

def set_note(track, note=60, channel=0, velocity=64, duration=480):
    track.append(Message('note_on', note=note, channel=channel, velocity=velocity, time=0))
    track.append(Message('note_off', note=note, channel=channel, velocity=127, time=duration))
    
def set_note_on(track, note=60, channel=0, velocity=64, duration=480):
    track.append(Message('note_on', note=note, channel=channel, velocity=velocity, time=0))
    track.append(Message('note_on', note=0, channel=channel, velocity=velocity, time=0))
    track.append(Message('note_off', note=0, channel=channel, velocity=127, time=duration))
    
def set_chord(track, root=60, chord=CHORDS['Major'], channel=0, velocity=64, duration=480):
    for offset in chord:
        track.append(Message('note_on', note=root+offset, channel=channel, velocity=velocity, time=0))
    for offset in chord:
        if offset == 0:
            time = duration
        else:
            time = 0
        track.append(Message('note_off', note=root+offset, channel=channel, velocity=127, time=time))
    
