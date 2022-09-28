from enum import Enum
import phimidi as pm

class Notes(Enum):
    C4 = 60
    D4 = 62


class Key():
    """
    generate classic key offsets for a root note
    """
    _pos = dict()

    def __init__(self, root: int):
        root = int(root)
        self.root = root
        self.I = root
        self.II = root + 2
        self.III = root + 4
        self.IV = root + 5
        self.V = root + 7
        self.VI = root + 9
        self.VII = root + 11

        self._pos[1] = self.I
        self._pos[2] = self.II
        self._pos[3] = self.III
        self._pos[4] = self.IV
        self._pos[5] = self.V
        self._pos[6] = self.VI
        self._pos[7] = self.VII

    def position(self, num: int):
        """
        numeric position
        """
        return self._pos[num]


a = Key(pm.N.C4)
print(a.V)
