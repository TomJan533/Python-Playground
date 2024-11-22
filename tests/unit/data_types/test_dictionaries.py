import pytest

@pytest.mark.unit
def test_dict_creation():
    assert isinstance({}, dict)
    assert isinstance({"key": "value"}, dict)

@pytest.mark.unit
def test_dict_length():
    data = {"a": 1, "b": 2, "c": 3}
    assert len(data) == 3
    assert len({}) == 0

@pytest.mark.unit
def test_dict_access():
    data = {"name": "Alice", "age": 30}
    assert data["name"] == "Alice"
    assert data["age"] == 30

@pytest.mark.unit
def test_dict_update():
    data = {"key": "value"}
    data["key"] = "new_value"  # Update existing key
    assert data["key"] == "new_value"

    data["new_key"] = "another_value"  # Add a new key
    assert data["new_key"] == "another_value"

@pytest.mark.unit
def test_dict_get():
    data = {"a": 1, "b": 2}
    assert data.get("a") == 1
    assert data.get("c") is None  # Key does not exist
    assert data.get("c", "default") == "default"  # Provide default value

@pytest.mark.unit
def test_dict_pop():
    data = {"a": 1, "b": 2}
    value = data.pop("a")  # Remove and return the value of the key
    assert value == 1
    assert "a" not in data

@pytest.mark.unit
def test_dict_clear():
    data = {"a": 1, "b": 2}
    data.clear()  # Remove all items
    assert len(data) == 0

@pytest.mark.unit
def test_dict_keys():
    data = {"a": 1, "b": 2}
    keys = data.keys()
    assert set(keys) == {"a", "b"}

@pytest.mark.unit
def test_dict_values():
    data = {"a": 1, "b": 2}
    values = data.values()
    assert set(values) == {1, 2}

@pytest.mark.unit
def test_dict_items():
    data = {"a": 1, "b": 2}
    items = data.items()
    assert set(items) == {("a", 1), ("b", 2)}

@pytest.mark.unit
def test_dict_update_method():
    data1 = {"a": 1, "b": 2}
    data2 = {"b": 3, "c": 4}
    data1.update(data2)  # Merge data2 into data1
    assert data1 == {"a": 1, "b": 3, "c": 4}

@pytest.mark.unit
def test_dict_merge_operator():
    data1 = {"a": 1, "b": 2}
    data2 = {"b": 3, "c": 4}
    merged = {**data1, **data2}  # Merge using unpacking
    assert merged == {"a": 1, "b": 3, "c": 4}

@pytest.mark.unit
def test_empty_dict():
    empty = {}
    assert len(empty) == 0
    assert not empty  # Empty dictionaries are falsy

@pytest.mark.unit
def test_dict_with_none_key():
    data = {None: "value"}
    assert data[None] == "value"

@pytest.mark.unit
def test_dict_type():
    assert isinstance({"a": 1, "b": 2}, dict)

@pytest.mark.unit
def test_dict_from_keys():
    keys = ["a", "b", "c"]
    data = dict.fromkeys(keys, 0)  # Create dictionary with default values
    assert data == {"a": 0, "b": 0, "c": 0}

@pytest.mark.unit
def test_dict_conversion():
    pairs = [("a", 1), ("b", 2)]
    assert dict(pairs) == {"a": 1, "b": 2}  # Convert list of tuples to dict
