import pytest

@pytest.mark.unit
def test_tuple_creation():
    assert isinstance((), tuple)
    assert isinstance((1, 2, 3), tuple)

@pytest.mark.unit
def test_tuple_length():
    assert len((1, 2, 3)) == 3
    assert len(()) == 0

@pytest.mark.unit
def test_tuple_indexing():
    values = (10, 20, 30)
    assert values[0] == 10  # First element
    assert values[-1] == 30  # Last element

@pytest.mark.unit
def test_tuple_membership():
    items = ("apple", "banana", "cherry")
    assert "banana" in items
    assert "grape" not in items

@pytest.mark.unit
def test_tuple_slicing():
    values = (1, 2, 3, 4, 5)
    assert values[:3] == (1, 2, 3)  # First three elements
    assert values[3:] == (4, 5)  # Elements from index 3 onward
    assert values[1:4] == (2, 3, 4)  # Elements from index 1 to 3

@pytest.mark.unit
def test_tuple_immutability():
    # Step 1: Create a tuple
    values = (1, 2, 3)

    # Step 2: Attempt to modify an element (should raise TypeError)
    with pytest.raises(TypeError, match="does not support item assignment"):
        values[0] = 10  # Tuples are immutable

    # Step 3: Verify that the tuple remains unchanged
    assert values == (1, 2, 3)

@pytest.mark.unit
def test_tuple_packing_unpacking():
    packed = 1, 2, 3  # Tuple packing
    assert packed == (1, 2, 3)

    a, b, c = packed  # Tuple unpacking
    assert a == 1
    assert b == 2
    assert c == 3

@pytest.mark.unit
def test_tuple_count():
    values = (1, 2, 2, 3, 2)
    assert values.count(2) == 3  # Count occurrences of 2

@pytest.mark.unit
def test_tuple_index():
    values = (10, 20, 30)
    assert values.index(20) == 1  # Index of first occurrence

@pytest.mark.unit
def test_tuple_equality():
    assert (1, 2, 3) == (1, 2, 3)
    assert (1, 2, 3) != (3, 2, 1)

@pytest.mark.unit
def test_tuple_lexicographical_comparison():
    assert (1, 2, 3) < (1, 2, 4)
    assert (1, 2, 3) > (1, 2, 2)

@pytest.mark.unit
def test_empty_tuple():
    empty = ()
    assert len(empty) == 0
    assert not empty  # Empty tuples are falsy

@pytest.mark.unit
def test_single_element_tuple():
    single = (42,)  # Note the comma to differentiate from int
    assert isinstance(single, tuple)
    assert single[0] == 42

@pytest.mark.unit
def test_nested_tuples():
    nested = ((1, 2), (3, 4))
    assert len(nested) == 2
    assert nested[0] == (1, 2)
    assert nested[1][1] == 4

@pytest.mark.unit
def test_tuple_type():
    assert isinstance((1, 2, 3), tuple)

@pytest.mark.unit
def test_tuple_conversion():
    assert tuple("abc") == ("a", "b", "c")
    assert tuple([1, 2, 3]) == (1, 2, 3)
