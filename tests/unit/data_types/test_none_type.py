"""
NoneType in Python:
--------------------
- `None` is a singleton object of type `NoneType` in Python.
- It represents the absence of a value or a null value.

Popular Use Cases:
-------------------
1. **Default Return Value**:
   - Functions without a `return` statement return `None` by default.

2. **Placeholders**:
   - Used as a placeholder for variables or arguments to indicate that they are intentionally empty or unset.

3. **Comparisons**:
   - Used in conditional statements to check for missing values.

4. **Data Structures**:
   - Commonly used in lists, dictionaries, or other collections to represent missing or undefined data.
"""
import pytest

@pytest.mark.unit
def test_none_type():
    assert isinstance(None, type(None))  # `None` is of type `NoneType`

@pytest.mark.unit
def test_none_equality():
    assert None is None  # `None` is a singleton
    assert None == None  # Equal comparison
    assert None is not True  # `None` is not `True`
    assert None is not False  # `None` is not `False`

@pytest.mark.unit
def test_function_returns_none():
    def my_function():
        pass  # No return statement

    assert my_function() is None  # Functions without `return` return `None`

@pytest.mark.unit
def test_function_with_none_default():
    def my_function(arg=None):
        return arg

    assert my_function() is None
    assert my_function(42) == 42

@pytest.mark.unit
def test_none_in_conditions():
    value = None
    if value is None:
        result = "Missing"
    else:
        result = "Present"
    assert result == "Missing"

@pytest.mark.unit
def test_none_in_list():
    data = [1, None, 3]
    assert len(data) == 3
    assert data[1] is None

@pytest.mark.unit
def test_none_in_dict():
    data = {"key1": None, "key2": 42}
    assert "key1" in data
    assert data["key1"] is None
    assert data["key2"] == 42

@pytest.mark.unit
def test_none_comparisons():
    assert None is None
    assert None != 0  # `None` is not equal to zero
    assert None != ""  # `None` is not equal to an empty string

    # Ensure unsupported comparisons raise TypeError
    with pytest.raises(TypeError, match="'<' not supported between instances of 'NoneType' and 'int'"):
        _ = None < 1

    with pytest.raises(TypeError, match="'>' not supported between instances of 'NoneType' and 'int'"):
        _ = None > 1

@pytest.mark.unit
def test_none_with_boolean():
    assert bool(None) is False  # `None` is falsy

@pytest.mark.unit
def test_none_identity():
    a = None
    b = None
    assert a is b  # `None` is a singleton, so all instances point to the same object
