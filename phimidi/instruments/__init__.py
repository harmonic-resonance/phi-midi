"""
wrapper for managing instruments
"""
import phimidi as pm
import phimidi.instruments.instrument_types as I
from phimidi.instruments.instrument import *


def make_piano(mf, channel):
    return pm.Instrument(mf, pm.I.acoustic_grand_piano, channel)

def make_vibes(mf, channel):
    return pm.Instrument(mf, pm.I.vibraphone, channel)

def make_bass(mf, channel):
    return pm.Instrument(mf, pm.I.acoustic_bass, channel)

def make_horns(mf, channel):
    return pm.Instrument(mf, pm.I.brass_section, channel)

def make_strings(mf, channel):
    return pm.Instrument(mf, pm.I.string_ensemble_1, channel)

