import pytest

@pytest.mark.unit
def test_complex_addition():
    result = (1 + 2j) + (3 + 4j)
    assert result == 4 + 6j

@pytest.mark.unit
def test_complex_subtraction():
    result = (5 + 6j) - (2 + 3j)
    assert result == 3 + 3j

@pytest.mark.unit
def test_complex_multiplication():
    result = (2 + 3j) * (4 + 5j)
    assert result == -7 + 22j

@pytest.mark.unit
def test_complex_division():
    result = (7 + 10j) / (1 + 2j)
    assert result == pytest.approx(5.4 - 0.8j, rel=1e-9)

@pytest.mark.unit
def test_complex_conjugate():
    z = 3 + 4j
    assert z.conjugate() == 3 - 4j

@pytest.mark.unit
def test_complex_real_part():
    z = 5 + 6j
    assert z.real == 5

@pytest.mark.unit
def test_complex_imaginary_part():
    z = 5 + 6j
    assert z.imag == 6


@pytest.mark.unit
def test_complex_zero():
    z = 0 + 0j
    assert z.real == 0
    assert z.imag == 0
    assert isinstance(z, complex)

@pytest.mark.unit
def test_complex_negative():
    z = -3 - 4j
    assert z.real == -3
    assert z.imag == -4

# type safety
@pytest.mark.unit
def test_complex_type():
    z = 1 + 2j
    assert isinstance(z, complex)

@pytest.mark.unit
def test_complex_conversion():
    z = complex(3, 4)
    assert z == 3 + 4j

    z = complex(5)
    assert z == 5 + 0j

    z = complex(0, -7)
    assert z == 0 - 7j

@pytest.mark.unit
def test_complex_abs():
    # Step 1: Define the complex number
    # z is a complex number with a real part of 3 and an imaginary part of 4.
    z = 3 + 4j  # z = 3 + 4j

    # Step 2: Calculate the magnitude of z
    # The magnitude of a complex number is calculated using the formula:
    # |z| = sqrt(real^2 + imag^2)
    # For z = 3 + 4j:
    # real = 3, imag = 4
    # |z| = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5
    magnitude = abs(z)  # magnitude = 5.0

    # Step 3: Assert the magnitude is as expected
    # Compare the calculated magnitude (5.0) with the expected value (5).
    assert magnitude == 5  # Passes because 5.0 == 5

    # Mid-step results:
    # z.real = 3
    # z.imag = 4
    # magnitude = 5.0
    # Expected value = 5
    # Result: Test passes since the magnitude matches the expected value.

@pytest.mark.unit
def test_complex_pow():
    z = 1 + 1j
    assert z**2 == 0 + 2j

@pytest.mark.unit
def test_complex_equality():
    z1 = 3 + 4j
    z2 = 3 + 4j
    assert z1 == z2
