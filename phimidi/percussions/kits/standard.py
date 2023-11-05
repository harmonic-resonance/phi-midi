#  import phimidi as pm
from .kit import Kit
from ..percussion import Percussion
import phimidi.percussions.percussion_types as P


class Standard(Kit):
    kit = []

    def __init__(self, part):
        """TODO: Docstring for __init__."""
        self.kick = Percussion(part, P.acoustic_bass_drum)
        self.kit.append(self.kick)

        self.snare = Percussion(part, P.acoustic_snare)
        self.kit.append(self.snare)

        self.closed_hh = Percussion(part, P.closed_hi_hat)
        self.kit.append(self.closed_hh)

        self.open_hh = Percussion(part, P.open_hi_hat)
        self.kit.append(self.open_hh)

    def billie_jean(self, duration: int, velocity_mod: int = 0):
        """2 measure

        :duration: time for phrase in milliseconds
        """
        b = int(duration / 16)
        pattern = "7_______" + "7_______"
        self.kick.add_pattern(pattern, b, velocity_mod=velocity_mod)

        pattern = "____7___" + "____7___"
        self.snare.add_pattern(pattern, b, velocity_mod=velocity_mod)

        pattern = "3_3_3_3_" + "3_3_3_3_"
        self.closed_hh.add_pattern(pattern, b, velocity_mod=velocity_mod)

        pattern = "________" + "________"
        self.open_hh.add_pattern(pattern, b, velocity_mod=velocity_mod)

    def funky_drummer(self, duration: int, velocity_mod: int = 0):
        """4 measure

        :duration: time for phrase in milliseconds
        """
        b = int(duration / 16)
        pattern = "7_5___7_" + "__5__7__"
        self.kick.add_pattern(pattern, b, velocity_mod=velocity_mod)

        pattern = "____7__5" + "_5_57__7"
        self.snare.add_pattern(pattern, b, velocity_mod=velocity_mod)

        pattern = "3232323_" + "32323_32"
        self.closed_hh.add_pattern(pattern, b, velocity_mod=velocity_mod)

        pattern = "_______5" + "_____5__"
        self.open_hh.add_pattern(pattern, b, velocity_mod=velocity_mod)
