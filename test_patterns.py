"""
script for generating accompaniment for Thelio videos
:bpm: based on the observed timing of the suspend light
"""
import phimidi as pm
import itertools as itertools
import random as random
from rich import print as log

PROJECT = 'test_patterns'
bpm = 180  # beats per minute
bpM = 4  # beats per Measure
root = pm.N.D3  # the root note of the key
key = 'D'

part = pm.Part(PROJECT, 'son_clave', bpm=bpm, root=root, key=key)
M = bpM * part.ticks_per_beat  # ticks per Measure

clave = pm.Percussion(part, pm.P.claves)
shaker = pm.Percussion(part, pm.P.shaker)

class Conga():
    '''conga kit - 2 drums + mute'''
    kit = []

    def __init__(self, part):
        """TODO: Docstring for __init__.
        """
        self.tumba = pm.Percussion(part, pm.P.low_conga)
        self.kit.append(self.tumba)

        self.conga = pm.Percussion(part, pm.P.open_hi_conga)
        self.kit.append(self.conga)

        self.mute_conga = pm.Percussion(part, pm.P.mute_hi_conga)
        self.kit.append(self.mute_conga)

    def tumbao(self, duration: int, velocity_mod: int=0):
        """2 measure tumbao rhythm

        :duration: TODO
        """
        b = int(duration/16)
        # 5 heel 4 toe
        mute =  '54_454__' + '54___4__'
        # 7 slap - 5 open
        conga = '__7___55' + '__7___55'
        tumba = '________' + '___77___'

        self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    def guaguanco(self, duration: int, velocity_mod: int=0):
        """2 measure tumbao rhythm

        :duration: TODO
        """
        b = int(duration/16)
        # 5 heel 4 toe 3 touch
        mute =  '___5_3__' + '_____3__'
        # 7 slap - 5 open
        conga = '_77___55' + '__7___55'
        tumba = '______7_' + '______8_'

        self.mute_conga.add_pattern(mute, b, velocity_mod=velocity_mod)
        self.conga.add_pattern(conga, b, velocity_mod=velocity_mod)
        self.tumba.add_pattern(tumba, b, velocity_mod=velocity_mod)

    def rest_all(self, duration: int):
        """TODO: Docstring for rest_all.

        :duration: TODO
        :returns: TODO

        """
        duration = int(duration)
        for perc in self.kit:
            perc.set_rest(duration)


conga = Conga(part)

#  part.set_marker(f'count', 0)
clave.set_hits(M, 4)
conga.rest_all(M)
shaker.set_rest(M)

for i in range(4):
    if i % 2:
        #  conga.tumbao(2 * M, velocity_mod=-10)
        conga.tumbao(2 * M)
        #  conga.guaguanco(2 * M)
    else:
        #  conga.tumbao(2 * M)
        conga.guaguanco(2 * M)

    pm.patterns.latin.son_clave2(2 * M, clave)
    for _ in range(4):
        shaker.set_hit(M/4, velocity=90)
        shaker.set_hit(M/4, velocity=60)

part.save()
part.play()
