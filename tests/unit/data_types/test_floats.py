import pytest

@pytest.mark.unit
def test_float_addition():
    assert 0.1 + 0.2 == pytest.approx(0.3)  # Using pytest.approx for precision issues

@pytest.mark.unit
def test_float_subtraction():
    assert 5.5 - 2.2 == pytest.approx(3.3)

@pytest.mark.unit
def test_float_multiplication():
    assert 1.5 * 2 == 3.0

@pytest.mark.unit
def test_float_division():
    assert 5.0 / 2.0 == 2.5

@pytest.mark.unit
def test_float_floor_division():
    assert 5.5 // 2 == 2.0  # Floor division truncates the decimal

@pytest.mark.unit
def test_float_modulus():
    assert 5.5 % 2 == pytest.approx(1.5)

@pytest.mark.unit
def test_float_exponentiation():
    assert 2.5 ** 2 == 6.25

@pytest.mark.unit
def test_float_equality():
    assert 1.1 + 2.2 == pytest.approx(3.3)  # Approximation due to floating-point imprecision

@pytest.mark.unit
def test_float_inequality():
    assert 3.5 != 2.5

@pytest.mark.unit
def test_float_greater_than():
    assert 4.5 > 4.0

@pytest.mark.unit
def test_float_less_than():
    assert 1.2 < 1.3

@pytest.mark.unit
def test_float_greater_than_or_equal():
    assert 2.5 >= 2.5

@pytest.mark.unit
def test_float_less_than_or_equal():
    assert 0.5 <= 0.5

@pytest.mark.unit
def test_float_zero():
    assert 0.0 == 0.0
    assert isinstance(0.0, float)

@pytest.mark.unit
def test_float_negative():
    assert -5.5 < 0.0

@pytest.mark.unit
def test_large_float():
    large_float = 1.79e308  # Close to float's maximum value
    assert isinstance(large_float, float)
    assert large_float > 1e307

@pytest.mark.unit
def test_small_float():
    small_float = 1.79e-308  # Close to float's minimum positive value
    assert isinstance(small_float, float)
    assert small_float > 0

# type safety
@pytest.mark.unit
def test_float_type():
    x = 3.14
    assert isinstance(x, float)

@pytest.mark.unit
def test_float_conversion():
    assert float("3.14") == 3.14
    assert float(10) == 10.0

# precision handling
@pytest.mark.unit
def test_float_precision():
    # Step 1: Perform the addition
    # 0.1 and 0.2 are floating-point numbers that cannot be represented
    # exactly in binary. Their addition results in a value close to 0.3 but not exactly 0.3.
    result = 0.1 + 0.2  # Result: 0.30000000000000004 (floating-point imprecision)
    
    # Step 2: Compare the result with 0.3 using pytest.approx
    # pytest.approx allows us to compare floating-point numbers within a certain relative or absolute tolerance.
    # rel=1e-9 means the comparison will tolerate differences up to 1 part in a billion.
    assert result == pytest.approx(0.3, rel=1e-9)

    # Mid-step debugging:
    # result = 0.30000000000000004
    # pytest.approx(0.3, rel=1e-9) defines an acceptable range: [0.2999999997, 0.3000000003]
    # Since 0.30000000000000004 falls within this range, the assertion passes.

    # Final Outcome: The test passes because the small floating-point error (4e-17)
    # is within the acceptable relative tolerance of 1e-9.
