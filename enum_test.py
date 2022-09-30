from enum import Enum
import phimidi as pm
from rich import print as log

class Notes(Enum):
    C4 = 60
    D4 = 62

session = pm.Session('test')
log(session)

#  session.save('test', 'test.mid')

log(session.free_channels)
