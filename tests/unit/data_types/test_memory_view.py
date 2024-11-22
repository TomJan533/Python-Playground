"""
Memory View in Python:
-----------------------
- `memoryview` is a built-in type that allows you to access the memory of an object without copying it.
- It works with objects that support the buffer protocol, such as `bytes`, `bytearray`, and other binary data.

Popular Use Cases:
-------------------
1. **Zero-Copy Slicing**:
   - Perform efficient slicing and manipulation of large binary data without duplicating it.

2. **Interfacing with Binary Data**:
   - Useful for low-level programming, such as interacting with hardware or binary file formats.

3. **Efficient Memory Sharing**:
   - Share memory between data structures, minimizing overhead.
"""
import pytest


@pytest.mark.unit
def test_memoryview_creation():
    data = b"hello"
    mv = memoryview(data)
    assert isinstance(mv, memoryview)

@pytest.mark.unit
def test_memoryview_length():
    data = b"hello"
    mv = memoryview(data)
    assert len(mv) == 5

@pytest.mark.unit
def test_memoryview_slice():
    data = b"hello"
    mv = memoryview(data)
    assert mv[0:2].tobytes() == b"he"  # Slice and convert back to bytes

@pytest.mark.unit
def test_memoryview_modify():
    data = bytearray(b"hello")
    mv = memoryview(data)
    mv[0] = 72  # ASCII for 'H'
    assert data == bytearray(b"Hello")

@pytest.mark.unit
def test_memoryview_tobytes():
    data = b"hello"
    mv = memoryview(data)
    assert mv.tobytes() == b"hello"  # Convert memoryview back to bytes

@pytest.mark.unit
def test_memoryview_hex():
    data = b"\x00\x01\x02"
    mv = memoryview(data)
    assert mv.hex() == "000102"  # Hexadecimal representation

@pytest.mark.unit
def test_memoryview_from_bytearray():
    data = bytearray(b"hello")
    mv = memoryview(data)
    assert mv.tobytes() == b"hello"

@pytest.mark.unit
def test_memoryview_from_bytes():
    data = b"hello"
    mv = memoryview(data)
    assert mv.tobytes() == b"hello"

@pytest.mark.unit
def test_memoryview_immutable():
    data = b"hello"  # Immutable bytes
    mv = memoryview(data)
    with pytest.raises(TypeError, match="cannot modify read-only memory"):
        mv[0] = 72  # Attempting to modify immutable data

@pytest.mark.unit
def test_memoryview_slicing():
    data = b"abcdef"
    mv = memoryview(data)
    sliced = mv[1:4]  # Slice from index 1 to 3
    assert sliced.tobytes() == b"bcd"

@pytest.mark.unit
def test_memoryview_comparison():
    mv1 = memoryview(b"hello")
    mv2 = memoryview(b"hello")
    assert mv1 == mv2  # Memory views with the same content are equal

@pytest.mark.unit
def test_empty_memoryview():
    data = b""
    mv = memoryview(data)
    assert len(mv) == 0
    assert mv.tobytes() == b""

@pytest.mark.unit
def test_memoryview_with_large_data():
    data = bytearray(range(256))  # 0 to 255
    mv = memoryview(data)
    assert len(mv) == 256
    assert mv[0] == 0
    assert mv[-1] == 255
