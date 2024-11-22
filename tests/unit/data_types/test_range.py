"""
Range in Python:
-----------------
- `range` represents an immutable sequence of numbers, commonly used for iteration in loops.
- It is memory-efficient as it does not store all elements in memory but generates them on demand.

Popular Use Cases:
-------------------
1. **Iteration**:
   - Used in `for` loops to iterate over a sequence of numbers.

2. **Lazy Sequences**:
   - Efficiently generate large sequences without storing them in memory.

3. **Indexing and Slicing**:
   - Access individual elements or slices like lists, but remains immutable.

4. **Mathematical Sequences**:
   - Generate arithmetic progressions with specified start, stop, and step values.
"""
import pytest

@pytest.mark.unit
def test_range_creation():
    assert isinstance(range(10), range)
    assert list(range(5)) == [0, 1, 2, 3, 4]  # Default start is 0
    assert list(range(2, 6)) == [2, 3, 4, 5]  # Start at 2, end before 6
    assert list(range(1, 10, 2)) == [1, 3, 5, 7, 9]  # Step of 2

@pytest.mark.unit
def test_range_indexing():
    r = range(5)
    assert r[0] == 0  # First element
    assert r[-1] == 4  # Last element

@pytest.mark.unit
def test_range_slicing():
    r = range(10)
    assert list(r[:5]) == [0, 1, 2, 3, 4]  # First 5 elements
    assert list(r[5:]) == [5, 6, 7, 8, 9]  # Elements from index 5 onward
    assert list(r[::2]) == [0, 2, 4, 6, 8]  # Every second element

@pytest.mark.unit
def test_range_equality():
    assert range(5) == range(0, 5, 1)  # Equivalent ranges
    assert range(1, 5) != range(0, 5)  # Start points differ

@pytest.mark.unit
def test_range_contains():
    r = range(5)
    assert 3 in r
    assert 5 not in r  # End is exclusive

@pytest.mark.unit
def test_range_length():
    assert len(range(10)) == 10  # Length is the count of numbers
    assert len(range(1, 10, 2)) == 5  # Step determines the count

@pytest.mark.unit
def test_empty_range():
    assert len(range(0)) == 0  # No numbers in the range
    assert list(range(0)) == []

@pytest.mark.unit
def test_reverse_range():
    r = range(10, 0, -2)  # Start at 10, decrement by 2
    assert list(r) == [10, 8, 6, 4, 2]

@pytest.mark.unit
def test_large_range():
    r = range(1_000_000)  # Very large range
    assert len(r) == 1_000_000
    assert r[999_999] == 999_999

@pytest.mark.unit
def test_range_memory_efficiency():
    import sys
    r = range(1_000_000)
    lst = list(r)
    assert sys.getsizeof(r) < sys.getsizeof(lst)  # Range uses less memory
