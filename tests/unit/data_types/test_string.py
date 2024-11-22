import pytest

@pytest.mark.unit
def test_string_concatenation():
    assert "Hello, " + "World!" == "Hello, World!"

@pytest.mark.unit
def test_string_repetition():
    assert "Ha" * 3 == "HaHaHa"

@pytest.mark.unit
def test_string_length():
    assert len("Python") == 6

@pytest.mark.unit
def test_string_membership():
    assert "P" in "Python"
    assert "z" not in "Python"

@pytest.mark.unit
def test_string_indexing():
    word = "Python"
    assert word[0] == "P"  # First character
    assert word[-1] == "n"  # Last character

@pytest.mark.unit
def test_string_slicing():
    word = "Python"
    assert word[:2] == "Py"  # First two characters
    assert word[2:] == "thon"  # All characters from index 2 onwards
    assert word[1:4] == "yth"  # Characters from index 1 to 3

@pytest.mark.unit
def test_string_upper():
    assert "python".upper() == "PYTHON"

@pytest.mark.unit
def test_string_lower():
    assert "PYTHON".lower() == "python"

@pytest.mark.unit
def test_string_strip():
    assert "  Hello  ".strip() == "Hello"

@pytest.mark.unit
def test_string_replace():
    assert "Hello, World!".replace("World", "Python") == "Hello, Python!"

@pytest.mark.unit
def test_string_split():
    assert "a,b,c".split(",") == ["a", "b", "c"]

@pytest.mark.unit
def test_string_join():
    assert "-".join(["a", "b", "c"]) == "a-b-c"

@pytest.mark.unit
def test_string_equality():
    assert "Python" == "Python"
    assert "Python" != "python"

@pytest.mark.unit
def test_string_case_insensitive_equality():
    assert "Python".lower() == "python"

@pytest.mark.unit
def test_string_comparison():
    assert "apple" < "banana"  # Lexicographical order
    assert "apple" > "Apple"  # ASCII-based comparison

@pytest.mark.unit
def test_empty_string():
    assert len("") == 0
    assert "" + "Hello" == "Hello"

@pytest.mark.unit
def test_multiline_string():
    multiline = """This is
a multiline
string."""
    assert "multiline" in multiline

@pytest.mark.unit
def test_string_type():
    assert isinstance("Python", str)

@pytest.mark.unit
def test_string_conversion():
    assert str(123) == "123"
    assert str(45.67) == "45.67"
