"""
Enumerations in Python:
------------------------
- Enums (`enum.Enum`) are a way to define a set of symbolic names bound to unique, constant values.
- They are immutable and iterable, making them ideal for representing choices or states in an application.

Popular Use Cases:
-------------------
1. **Constants**:
   - Represent fixed sets of values, such as days of the week or directions.

2. **Type Safety**:
   - Avoids using arbitrary integers or strings, improving code clarity and reliability.

3. **Switches and Logic**:
   - Use enums in conditional statements to manage state or behavior.

Enumerations are defined using the `enum` module.
"""
import pytest
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

@pytest.mark.unit
def test_enum_members():
    assert Color.RED.name == "RED"
    assert Color.RED.value == 1
    assert Color.GREEN.name == "GREEN"
    assert Color.GREEN.value == 2

@pytest.mark.unit
def test_enum_iteration():
    members = list(Color)
    assert members == [Color.RED, Color.GREEN, Color.BLUE]

@pytest.mark.unit
def test_enum_comparison():
    assert Color.RED == Color.RED
    assert Color.RED != Color.BLUE
    assert Color.RED is not None

@pytest.mark.unit
def test_enum_access():
    assert Color["RED"] == Color.RED
    assert Color(1) == Color.RED

class Status(Enum):
    STARTED = auto()
    RUNNING = auto()
    COMPLETED = auto()

@pytest.mark.unit
def test_enum_auto():
    assert Status.STARTED.value == 1
    assert Status.RUNNING.value == 2
    assert Status.COMPLETED.value == 3

@pytest.mark.unit
def test_enum_in_condition():
    state = Color.RED
    if state == Color.RED:
        result = "Stop"
    elif state == Color.GREEN:
        result = "Go"
    else:
        result = "Caution"

    assert result == "Stop"

@pytest.mark.unit
def test_invalid_enum_access():
    with pytest.raises(KeyError, match=r"'INVALID'"):  # Match the actual KeyError message
        _ = Color["INVALID"]  # Accessing an invalid key raises KeyError


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    UP = 1  # Alias for NORTH

@pytest.mark.unit
def test_enum_alias():
    assert Direction.UP == Direction.NORTH  # Aliases are equal
    assert list(Direction) == [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]  # Aliases are excluded from iteration
