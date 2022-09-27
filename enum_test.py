from enum import Enum

class Notes(Enum):
    C4 = 60
    D4 = 62

print(list(Notes)[1])

print(Notes.C4.value)

print(Notes(60))

