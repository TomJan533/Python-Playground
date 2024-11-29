"""
This file demonstrates Python's dynamic typing and optional static typing.
It contains unit tests that illustrate how Python allows type changes at runtime
(dynamically typed) while also supporting static type annotations to improve code
quality and catch type errors early using tools like mypy.

The tests highlight:
1. Dynamic typing (variables can change types at runtime).
2. Static typing (type hints are optional and checked by static analyzers, not at runtime).
3. A comparison of dynamic behavior versus static type hinting.
4. Practical examples to discuss in technical interviews.
"""

# !NOTE: execute following line when uncommenting the mypy errors: 
# !$ poetry run mypy --strict tests/unit/test_typing.py

import pytest
from typing import List, Union


# Dynamic Typing: Python allows type changes at runtime.
@pytest.mark.unit
def test_dynamic_typing() -> None:
    variable: Union[int, str, List[int]] = 10  # Allow multiple types
    assert isinstance(variable, int)

    variable = "hello"
    assert isinstance(variable, str)

    variable = [1, 2, 3]
    assert isinstance(variable, list)


# Static Typing: Type hints are checked by tools like mypy, not at runtime.
def static_example(numbers: List[int]) -> int:
    return sum(numbers)


@pytest.mark.unit
def test_static_typing() -> None:
    # Function expects a list of integers
    result = static_example([1, 2, 3])
    assert result == 6

    # Demonstrating how mypy catches errors
    # Uncomment the next line to see `mypy` error
    # result = static_example("123")


@pytest.mark.unit
def test_static_type_hinting() -> None:
    # Works with correct type
    assert static_example([1, 2, 3]) == 6

    # Uncomment to see the mypy error
    # result = static_example("123")


# Demonstrating Dynamic vs Static Typing
@pytest.mark.unit
def test_dynamic_behavior() -> None:
    variable: Union[int, str] = 42  # Initially an integer
    assert isinstance(variable, int)

    variable = "Now I'm a string!"  # Dynamically becomes a string
    assert isinstance(variable, str)

    # Add type annotations to the dynamically typed function
    def dynamically_typed_function(value: Union[int, str]) -> Union[int, str]:
        return value * 2

    assert dynamically_typed_function(3) == 6
    assert dynamically_typed_function("hello") == "hellohello"  # Works dynamically


def static_typing_example(numbers: List[int]) -> int:
    return sum(numbers)
