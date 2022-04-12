import phimidi as pm
from phimidi.voices.voice import *
import phimidi.voices.voice_types as V

def make_solo_ooh(mf):
    return pm.Voice(mf, voice_name=pm.V.solo_ooh)

def make_solo_aah(mf):
    return pm.Voice(mf, voice_name=pm.V.solo_aah)

def make_choir_aah(mf):
    return pm.Voice(mf, voice_name=pm.V.choir_aah)

def make_choir_ooh(mf):
    return pm.Voice(mf, voice_name=pm.V.choir_ooh)

def make_choir_mixed(mf):
    return pm.Voice(mf, voice_name=pm.V.choir_mixed)

def make_choir_swell(mf):
    return pm.Voice(mf, voice_name=pm.V.choir_swell)

def make_choir_little_swell(mf):
    return pm.Voice(mf, voice_name=pm.V.choir_little_swell)
