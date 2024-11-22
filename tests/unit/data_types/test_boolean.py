import pytest

@pytest.mark.unit
def test_boolean_true():
    assert True is True

@pytest.mark.unit
def test_boolean_false():
    assert False is False

@pytest.mark.unit
def test_boolean_not():
    assert not True is False
    assert not False is True

@pytest.mark.unit
def test_boolean_and():
    assert (True and True) == True
    assert (True and False) == False
    assert (False and True) == False
    assert (False and False) == False

@pytest.mark.unit
def test_boolean_or():
    assert True or True is True
    assert True or False is True
    assert False or True is True
    assert False or False is False


@pytest.mark.unit
def test_boolean_equality():
    assert (5 > 3) is True
    assert (5 < 3) is False

@pytest.mark.unit
def test_boolean_in_conditions():
    assert bool(1) is True  # Non-zero numbers are True
    assert bool(0) is False  # Zero is False
    assert bool([]) is False  # Empty lists are False
    assert bool([1, 2, 3]) is True  # Non-empty lists are True

@pytest.mark.unit
def test_boolean_type():
    assert isinstance(True, bool)
    assert isinstance(False, bool)

@pytest.mark.unit
def test_boolean_conversion():
    assert bool(1) is True
    assert bool(0) is False
    assert bool("Non-empty") is True
    assert bool("") is False
    
@pytest.mark.unit
def test_boolean_as_integers():
    assert (True + True) == 2  # True is treated as 1
    assert (True * 5) == 5
    assert (False + 10) == 10
    assert (False * 10) == 0

@pytest.mark.unit
def test_complex_boolean_expression():
    expression = (True and not False) or (False and True)
    assert expression is True

@pytest.mark.unit
def test_boolean_short_circuit():
    # 'or' short-circuits: doesn't evaluate the second operand if the first is True
    assert (True or 1 / 0) is True

    # 'and' short-circuits: doesn't evaluate the second operand if the first is False
    assert (False and 1 / 0) is False
