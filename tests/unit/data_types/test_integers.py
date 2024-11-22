import pytest

@pytest.mark.unit
def test_integer_addition():
    assert 5 + 3 == 8

@pytest.mark.unit
def test_integer_subtraction():
    assert 10 - 7 == 3

@pytest.mark.unit
def test_integer_multiplication():
    assert 4 * 3 == 12

@pytest.mark.unit
def test_integer_division():
    assert 10 // 2 == 5  # Integer division

@pytest.mark.unit
def test_integer_modulus():
    assert 10 % 3 == 1

@pytest.mark.unit
def test_integer_exponentiation():
    assert 2 ** 3 == 8


@pytest.mark.unit
def test_integer_equality():
    assert 10 == 10

@pytest.mark.unit
def test_integer_inequality():
    assert 10 != 5

@pytest.mark.unit
def test_integer_greater_than():
    assert 10 > 5

@pytest.mark.unit
def test_integer_less_than():
    assert 3 < 7

@pytest.mark.unit
def test_integer_greater_than_or_equal():
    assert 5 >= 5

@pytest.mark.unit
def test_integer_less_than_or_equal():
    assert 4 <= 4
    
@pytest.mark.unit
def test_negative_integer():
    assert -10 < 0

@pytest.mark.unit
def test_zero_is_integer():
    assert isinstance(0, int)

@pytest.mark.unit
def test_large_integer():
    large_number = 10**12
    assert isinstance(large_number, int)
    assert large_number > 0
    
# typesafety
@pytest.mark.unit
def test_integer_type():
    x = 42
    assert isinstance(x, int)

@pytest.mark.unit
def test_integer_conversion():
    assert int("123") == 123
    assert int(123.45) == 123