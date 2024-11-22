"""
Byte Arrays in Python:
-----------------------
- The `bytearray` type is a mutable sequence of bytes, with each value ranging from 0 to 255.
- Unlike `bytes`, `bytearray` can be modified in place, making it useful for scenarios requiring mutable binary data.

Popular Use Cases:
-------------------
1. **Mutable Binary Data**:
   - Useful for modifying binary data, such as editing file content or packet data.
2. **Performance**:
   - Efficient for in-place modifications to avoid creating new objects.
3. **Network and File Operations**:
   - Working with data buffers during network communication or binary file manipulation.
"""
import pytest

@pytest.mark.unit
def test_bytearray_creation():
    assert isinstance(bytearray(), bytearray)
    assert isinstance(bytearray(b"hello"), bytearray)
    assert isinstance(bytearray([104, 101, 108, 108, 111]), bytearray)

@pytest.mark.unit
def test_bytearray_length():
    data = bytearray(b"hello")
    assert len(data) == 5
    assert len(bytearray()) == 0

@pytest.mark.unit
def test_bytearray_mutability():
    data = bytearray(b"hello")
    data[0] = 72  # Modify the first byte (ASCII for 'H')
    assert data == bytearray(b"Hello")

@pytest.mark.unit
def test_bytearray_append():
    data = bytearray(b"hello")
    data.append(33)  # ASCII for '!'
    assert data == bytearray(b"hello!")

@pytest.mark.unit
def test_bytearray_extend():
    data = bytearray(b"hello")
    data.extend(b" world")
    assert data == bytearray(b"hello world")

@pytest.mark.unit
def test_bytearray_upper():
    data = bytearray(b"hello")
    assert data.upper() == bytearray(b"HELLO")

@pytest.mark.unit
def test_bytearray_replace():
    data = bytearray(b"hello world")
    result = data.replace(b"world", b"Python")
    assert result == bytearray(b"hello Python")

@pytest.mark.unit
def test_bytearray_split():
    data = bytearray(b"hello world")
    assert data.split() == [bytearray(b"hello"), bytearray(b"world")]

@pytest.mark.unit
def test_bytearray_concatenation():
    data1 = bytearray(b"hello")
    data2 = bytearray(b" world")
    result = data1 + data2
    assert result == bytearray(b"hello world")

@pytest.mark.unit
def test_bytearray_repetition():
    data = bytearray(b"ha")
    assert data * 3 == bytearray(b"hahaha")

@pytest.mark.unit
def test_bytes_to_bytearray():
    data = b"hello"
    assert bytearray(data) == bytearray(b"hello")

@pytest.mark.unit
def test_bytearray_to_bytes():
    data = bytearray(b"hello")
    assert bytes(data) == b"hello"

@pytest.mark.unit
def test_bytearray_is_mutable():
    data = bytearray(b"hello")
    data[1] = 79  # Modify the second byte (ASCII for 'O')
    assert data == bytearray(b"hOllo")

@pytest.mark.unit
def test_empty_bytearray():
    empty = bytearray()
    assert len(empty) == 0
    assert not empty  # Empty bytearrays are falsy

@pytest.mark.unit
def test_bytearray_with_null():
    data = bytearray(b"hello\x00world")
    assert len(data) == 11  # Includes the null byte
    assert data.split(b"\x00") == [bytearray(b"hello"), bytearray(b"world")]
