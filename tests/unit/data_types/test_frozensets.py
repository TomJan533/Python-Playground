"""
Frozensets in Python:
---------------------
- A frozenset is an immutable version of a set.
- It is hashable and can be used as a key in dictionaries or added to other sets.
- Unlike regular sets, frozensets do not support methods that modify the set, such as add(), remove(), or clear().
- Frozensets were introduced in Python 2.4. 

Use Cases:
----------
- Frozensets are ideal when you need a set that should remain constant after creation.
- Commonly used for maintaining unique, immutable collections, such as constants or keys in dictionaries.
"""

import pytest

@pytest.mark.unit
def test_frozenset_creation():
    assert isinstance(frozenset(), frozenset)
    assert isinstance(frozenset([1, 2, 3]), frozenset)

@pytest.mark.unit
def test_frozenset_length():
    numbers = frozenset([1, 2, 3])
    assert len(numbers) == 3
    assert len(frozenset()) == 0

@pytest.mark.unit
def test_frozenset_membership():
    fruits = frozenset(["apple", "banana", "cherry"])
    assert "banana" in fruits
    assert "grape" not in fruits

@pytest.mark.unit
def test_frozenset_immutable():
    numbers = frozenset([1, 2, 3])
    with pytest.raises(AttributeError, match="'frozenset' object has no attribute 'add'"):
        numbers.add(4)  # Frozen sets do not support mutation

    with pytest.raises(AttributeError, match="'frozenset' object has no attribute 'remove'"):
        numbers.remove(1)  # Frozen sets do not support mutation

@pytest.mark.unit
def test_frozenset_union():
    set1 = frozenset([1, 2, 3])
    set2 = frozenset([3, 4, 5])
    assert set1.union(set2) == frozenset([1, 2, 3, 4, 5])

@pytest.mark.unit
def test_frozenset_intersection():
    set1 = frozenset([1, 2, 3])
    set2 = frozenset([2, 3, 4])
    assert set1.intersection(set2) == frozenset([2, 3])

@pytest.mark.unit
def test_frozenset_difference():
    set1 = frozenset([1, 2, 3])
    set2 = frozenset([2, 3, 4])
    assert set1.difference(set2) == frozenset([1])

@pytest.mark.unit
def test_frozenset_symmetric_difference():
    set1 = frozenset([1, 2, 3])
    set2 = frozenset([2, 3, 4])
    assert set1.symmetric_difference(set2) == frozenset([1, 4])

@pytest.mark.unit
def test_frozenset_subset():
    set1 = frozenset([1, 2])
    set2 = frozenset([1, 2, 3])
    assert set1.issubset(set2) is True

@pytest.mark.unit
def test_frozenset_superset():
    set1 = frozenset([1, 2, 3])
    set2 = frozenset([1, 2])
    assert set1.issuperset(set2) is True

@pytest.mark.unit
def test_frozenset_disjoint():
    set1 = frozenset([1, 2])
    set2 = frozenset([3, 4])
    assert set1.isdisjoint(set2) is True

    set3 = frozenset([2, 3])
    assert set1.isdisjoint(set3) is False

@pytest.mark.unit
def test_empty_frozenset():
    empty = frozenset()
    assert len(empty) == 0
    assert not empty  # Empty frozensets are falsy

@pytest.mark.unit
def test_frozenset_with_duplicates():
    numbers = frozenset([1, 2, 2, 3])
    assert len(numbers) == 3  # Duplicates are removed
    assert numbers == frozenset([1, 2, 3])

@pytest.mark.unit
def test_frozenset_type():
    assert isinstance(frozenset([1, 2, 3]), frozenset)

@pytest.mark.unit
def test_frozenset_conversion():
    assert frozenset([1, 2, 3]) == frozenset({1, 2, 3})  # Convert set to frozenset
    assert frozenset("abc") == frozenset(["a", "b", "c"])  # Convert string to frozenset
