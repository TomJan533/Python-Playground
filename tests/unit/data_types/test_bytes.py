"""
Bytes in Python:
----------------
- `bytes` is an immutable sequence of bytes (8-bit values).
- Each element of a bytes object is an integer in the range 0-255.
- Bytes are used to represent binary data or text data in encoded formats.

Popular Use Cases:
------------------
1. **Binary Data Processing**: Reading and writing binary files (e.g., images, videos, executables).
2. **Data Transmission**: Sending and receiving data over network sockets or APIs.
3. **Encoding and Decoding**: Converting text (str) to bytes (e.g., UTF-8) for storage or transmission.
4. **Cryptography**: Working with encrypted data or hash functions which produce byte sequences.
5. **Low-Level I/O**: Interacting with hardware or protocols that require binary formats.
"""
import pytest

@pytest.mark.unit
def test_bytes_creation():
    assert isinstance(b"", bytes)
    assert isinstance(b"hello", bytes)

@pytest.mark.unit
def test_bytes_length():
    data = b"hello"
    assert len(data) == 5
    assert len(b"") == 0

@pytest.mark.unit
def test_bytes_indexing():
    data = b"hello"
    assert data[0] == 104  # ASCII value of 'h'
    assert data[-1] == 111  # ASCII value of 'o'

@pytest.mark.unit
def test_bytes_upper():
    data = b"hello"
    assert data.upper() == b"HELLO"

@pytest.mark.unit
def test_bytes_split():
    data = b"hello world"
    assert data.split() == [b"hello", b"world"]

@pytest.mark.unit
def test_bytes_replace():
    data = b"hello world"
    assert data.replace(b"world", b"Python") == b"hello Python"

@pytest.mark.unit
def test_bytes_immutability():
    data = b"hello"
    with pytest.raises(TypeError, match="'bytes' object does not support item assignment"):
        data[0] = 104  # Cannot modify bytes

@pytest.mark.unit
def test_bytes_concatenation():
    assert b"hello" + b" world" == b"hello world"

@pytest.mark.unit
def test_bytes_repetition():
    assert b"ha" * 3 == b"hahaha"

@pytest.mark.unit
def test_bytes_from_string():
    data = "hello".encode("utf-8")  # Convert string to bytes
    assert data == b"hello"

@pytest.mark.unit
def test_bytes_to_string():
    data = b"hello"
    assert data.decode("utf-8") == "hello"

@pytest.mark.unit
def test_bytes_equality():
    assert b"hello" == b"hello"
    assert b"hello" != b"world"

@pytest.mark.unit
def test_bytes_lexicographical_comparison():
    assert b"apple" < b"banana"
    assert b"apple" > b"APPLE"  # Case-sensitive comparison

@pytest.mark.unit
def test_bytes_ascii_values():
    data = b"abc"
    assert [ord(c) for c in "abc"] == [97, 98, 99]  # ASCII values
    assert list(data) == [97, 98, 99]  # Same as ASCII values of 'a', 'b', 'c'

@pytest.mark.unit
def test_empty_bytes():
    empty = b""
    assert len(empty) == 0
    assert not empty  # Empty bytes are falsy

@pytest.mark.unit
def test_bytes_with_null():
    data = b"hello\x00world"
    assert len(data) == 11  # Includes the null byte
    assert data.split(b"\x00") == [b"hello", b"world"]

@pytest.mark.unit
def test_bytes_type():
    assert isinstance(b"hello", bytes)
    assert isinstance(bytes("hello", "utf-8"), bytes)
