import pytest

@pytest.mark.unit
def test_list_creation():
    assert isinstance([], list)
    assert isinstance([1, 2, 3], list)

@pytest.mark.unit
def test_list_length():
    assert len([1, 2, 3]) == 3
    assert len([]) == 0

@pytest.mark.unit
def test_list_indexing():
    numbers = [10, 20, 30]
    assert numbers[0] == 10  # First element
    assert numbers[-1] == 30  # Last element

@pytest.mark.unit
def test_list_membership():
    fruits = ["apple", "banana", "cherry"]
    assert "banana" in fruits
    assert "grape" not in fruits

@pytest.mark.unit
def test_list_slicing():
    numbers = [1, 2, 3, 4, 5]
    assert numbers[:3] == [1, 2, 3]  # First three elements
    assert numbers[3:] == [4, 5]  # Elements from index 3 onward
    assert numbers[1:4] == [2, 3, 4]  # Elements from index 1 to 3

@pytest.mark.unit
def test_list_append():
    numbers = [1, 2]
    numbers.append(3)
    assert numbers == [1, 2, 3]

@pytest.mark.unit
def test_list_extend():
    numbers = [1, 2]
    numbers.extend([3, 4])
    assert numbers == [1, 2, 3, 4]

@pytest.mark.unit
def test_list_insert():
    numbers = [1, 3]
    numbers.insert(1, 2)
    assert numbers == [1, 2, 3]

@pytest.mark.unit
def test_list_remove():
    fruits = ["apple", "banana", "cherry"]
    fruits.remove("banana")
    assert fruits == ["apple", "cherry"]

@pytest.mark.unit
def test_list_pop():
    numbers = [1, 2, 3]
    popped = numbers.pop()
    assert popped == 3
    assert numbers == [1, 2]

@pytest.mark.unit
def test_list_sort():
    numbers = [3, 1, 4, 2]
    numbers.sort()
    assert numbers == [1, 2, 3, 4]

@pytest.mark.unit
def test_list_reverse():
    numbers = [1, 2, 3]
    numbers.reverse()
    assert numbers == [3, 2, 1]

@pytest.mark.unit
def test_list_equality():
    assert [1, 2, 3] == [1, 2, 3]
    assert [1, 2, 3] != [3, 2, 1]

@pytest.mark.unit
def test_list_lexicographical_comparison():
    assert [1, 2, 3] < [1, 2, 4]  # Element-wise comparison
    assert [1, 2, 3] > [1, 2, 2]

@pytest.mark.unit
def test_empty_list():
    empty_list = []
    assert len(empty_list) == 0
    assert not empty_list  # Empty lists are falsy

@pytest.mark.unit
def test_nested_lists():
    nested = [[1, 2], [3, 4]]
    assert len(nested) == 2
    assert nested[0] == [1, 2]
    assert nested[1][1] == 4


@pytest.mark.unit
def test_list_type():
    assert isinstance([1, 2, 3], list)

@pytest.mark.unit
def test_list_conversion():
    assert list("abc") == ["a", "b", "c"]
    assert list((1, 2, 3)) == [1, 2, 3]
