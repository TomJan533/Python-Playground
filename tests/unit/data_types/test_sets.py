import pytest

@pytest.mark.unit
def test_set_creation():
    assert isinstance(set(), set)
    assert isinstance({1, 2, 3}, set)

@pytest.mark.unit
def test_set_length():
    numbers = {1, 2, 3}
    assert len(numbers) == 3
    assert len(set()) == 0

@pytest.mark.unit
def test_set_membership():
    fruits = {"apple", "banana", "cherry"}
    assert "banana" in fruits
    assert "grape" not in fruits

@pytest.mark.unit
def test_set_add():
    numbers = {1, 2}
    numbers.add(3)
    assert numbers == {1, 2, 3}

@pytest.mark.unit
def test_set_remove():
    numbers = {1, 2, 3}
    numbers.remove(2)
    assert numbers == {1, 3}

@pytest.mark.unit
def test_set_discard():
    numbers = {1, 2, 3}
    numbers.discard(2)  # Removes element if present; no error if not
    assert numbers == {1, 3}

    numbers.discard(4)  # No error if 4 is not in the set
    assert numbers == {1, 3}

@pytest.mark.unit
def test_set_clear():
    numbers = {1, 2, 3}
    numbers.clear()
    assert len(numbers) == 0

@pytest.mark.unit
def test_set_union():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    assert set1.union(set2) == {1, 2, 3, 4, 5}

@pytest.mark.unit
def test_set_intersection():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    assert set1.intersection(set2) == {2, 3}

@pytest.mark.unit
def test_set_difference():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    assert set1.difference(set2) == {1}

@pytest.mark.unit
def test_set_symmetric_difference():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    assert set1.symmetric_difference(set2) == {1, 4}

@pytest.mark.unit
def test_set_subset():
    set1 = {1, 2}
    set2 = {1, 2, 3}
    assert set1.issubset(set2) is True

@pytest.mark.unit
def test_set_superset():
    set1 = {1, 2, 3}
    set2 = {1, 2}
    assert set1.issuperset(set2) is True

@pytest.mark.unit
def test_set_disjoint():
    set1 = {1, 2}
    set2 = {3, 4}
    assert set1.isdisjoint(set2) is True

    set3 = {2, 3}
    assert set1.isdisjoint(set3) is False

@pytest.mark.unit
def test_empty_set():
    empty = set()
    assert len(empty) == 0
    assert not empty  # Empty sets are falsy

@pytest.mark.unit
def test_set_with_duplicates():
    numbers = {1, 2, 2, 3}
    assert len(numbers) == 3  # Duplicates are removed
    assert numbers == {1, 2, 3}

@pytest.mark.unit
def test_set_type():
    assert isinstance({1, 2, 3}, set)

@pytest.mark.unit
def test_set_conversion():
    assert set([1, 2, 2, 3]) == {1, 2, 3}  # Convert list to set
    assert set("abc") == {"a", "b", "c"}  # Convert string to set
