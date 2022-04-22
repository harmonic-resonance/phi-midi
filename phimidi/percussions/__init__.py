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



def deep_house(length, kick, clap, hihat_closed, hihat_open):
    length = int(length)
    b = int(length/32)
    kick.set_hits(length, 8, velocity=90)

    hihat_open.set_rest(2 * b)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(4 * b, velocity=60)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(4 * b, velocity=60)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(4 * b, velocity=60)
    hihat_open.set_hit(4 * b, velocity=90)
    hihat_open.set_hit(2 * b, velocity=60)

    hihat_closed.set_rest(1 * b)
    hihat_closed.set_hit(6 * b, velocity=90)
    hihat_closed.set_hit(2 * b, velocity=60)
    hihat_closed.set_hit(8 * b, velocity=60)
    hihat_closed.set_hit(6 * b, velocity=90)
    hihat_closed.set_hit(2 * b, velocity=60)
    hihat_closed.set_hit(7 * b, velocity=60)

    clap.set_rest(4 * b)
    clap.set_hit(8 * b, velocity=90)
    clap.set_hit(8 * b, velocity=90)
    clap.set_hit(8 * b, velocity=90)
    clap.set_hit(4 * b, velocity=90)

def drum_bass(length, kick, snare, hihat_closed, hihat_open):
    length = int(length)
    b = int(length/32)
    hihat_open.set_hit(length, velocity=90)
    kick.set_hit(6 * b, velocity=90)
    kick.set_hit(10 * b, velocity=70)
    kick.set_hit(10 * b, velocity=90)
    kick.set_hit(6 * b, velocity=70)
    hihat_closed.set_hits(length, 16)
    snare.set_rest(4 * b)
    snare.set_hit(6 * b, velocity=90)
    snare.set_hit(2 * b, velocity=60)
    snare.set_hit(8 * b, velocity=60)
    snare.set_hit(8 * b, velocity=90)
    snare.set_hit(4 * b, velocity=60)

