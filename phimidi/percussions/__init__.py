'''
https://docs.google.com/spreadsheets/d/19_3BxUMy3uy1Gb0V8Wc-TcG7q16Amfn6e8QVw4-HuD0/edit#gid=0
'''
from . import percussion_types as P
from . import patterns
from .percussion import Percussion

def make_tick(mf):
    return Percussion(mf, P.side_stick)

def make_kick(mf):
    return Percussion(mf, P.acoustic_bass_drum)

def make_snare(mf):
    return Percussion(mf, P.acoustic_snare)

def make_hihat_closed(mf):
    return Percussion(mf, P.closed_hi_hat)

def make_ride(mf):
    return Percussion(mf, P.ride_cymbal_1)



