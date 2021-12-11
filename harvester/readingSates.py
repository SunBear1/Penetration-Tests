from enum import Enum


class State(Enum):
    INITIAL = 0
    VALID_I = 1
    AT = 2
    VALID_II = 3
    INVALID = 4
