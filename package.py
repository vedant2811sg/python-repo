from enum import Enum


class State(Enum):
    """Enum representing the state of a package."""
    INACTIVE = 0
    ACTIVE = 1  

print(State.INACTIVE)  # Output: State.INACTIVE
print(State['ACTIVE'])  # Output: State.ACTIVE
print(State['ACTIVE'].value)  # Output: 1
