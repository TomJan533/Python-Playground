import pytest

# Helper function to create a generator
def sample_generator():
    yield 1
    yield 2
    yield 3

@pytest.mark.unit
def test_generator_creation():
    gen = sample_generator()
    assert hasattr(gen, "__iter__")  # Generators are iterable
    assert hasattr(gen, "__next__")  # Generators support the iterator protocol

@pytest.mark.unit
def test_generator_iteration():
    gen = sample_generator()
    
    # Step 1: Exhaust the generator
    assert next(gen) == 1  # First value
    assert next(gen) == 2  # Second value
    assert next(gen) == 3  # Third value

    # Step 2: Call `next()` again (generator is exhausted now)
    with pytest.raises(StopIteration):  # Assert that StopIteration is raised
        next(gen)

@pytest.mark.unit
def test_generator_exhaustion():
    gen = sample_generator()
    values = list(gen)  # Consume the generator
    assert values == [1, 2, 3]
    assert list(gen) == []  # Subsequent iterations yield nothing

@pytest.mark.unit
def test_generator_comprehension():
    gen = (x * 2 for x in range(3))  # Generator comprehension
    assert list(gen) == [0, 2, 4]

@pytest.mark.unit
def test_generator_membership():
    gen = (x for x in range(5))
    values = list(gen)
    assert 2 in values
    assert 5 not in values

@pytest.mark.unit
def test_generator_expression_short_circuit():
    gen = (x for x in range(5))
    assert next(gen) == 0  # Generators execute lazily
    assert next(gen) == 1  # Step through one value at a time

@pytest.mark.unit
def test_generator_slicing():
    gen = (x for x in range(10))
    assert list(gen)[:3] == [0, 1, 2]  # Generators can be converted to lists for slicing
    assert list(gen)[3:6] == []  # Generator is exhausted after first conversion

@pytest.mark.unit
def test_generator_unpacking():
    gen = sample_generator()
    a, b, c = gen  # Unpacking
    assert a == 1
    assert b == 2
    assert c == 3

@pytest.mark.unit
def test_generator_immutability():
    gen = sample_generator()
    with pytest.raises(TypeError):
        gen[0] = 42  # Generators do not support item assignment

@pytest.mark.unit
def test_generator_nested():
    def nested_generator():
        for i in range(3):
            yield (x for x in range(i, i + 2))

    nested_gen = nested_generator()
    first_gen = next(nested_gen)
    assert list(first_gen) == [0, 1]  # Nested generator output
    second_gen = next(nested_gen)
    assert list(second_gen) == [1, 2]

@pytest.mark.unit
def test_generator_empty():
    def empty_generator():
        if False:  # No conditions met
            yield
    gen = empty_generator()
    assert list(gen) == []  # No values produced

@pytest.mark.unit
def test_generator_reusability():
    gen = sample_generator()
    assert list(gen) == [1, 2, 3]
    assert list(gen) == []  # Generators cannot be reused

@pytest.mark.unit
def test_generator_with_condition():
    gen = (x for x in range(10) if x % 2 == 0)
    assert list(gen) == [0, 2, 4, 6, 8]  # Only even numbers

@pytest.mark.unit
def test_generator_custom_logic():
    def custom_generator():
        for i in range(5):
            yield i * i

    gen = custom_generator()
    assert list(gen) == [0, 1, 4, 9, 16]

@pytest.mark.unit
def test_generator_len_unsupported():
    gen = sample_generator()
    with pytest.raises(TypeError):
        len(gen)  # Generators do not support `len()`

@pytest.mark.unit
def test_generator_conversion_to_tuple():
    gen = (x for x in range(5))
    assert tuple(gen) == (0, 1, 2, 3, 4)  # Convert to tuple

@pytest.mark.unit
def test_generator_manual_control():
    def manual_generator():
        yield "a"
        yield "b"
        yield "c"

    gen = manual_generator()
    assert next(gen) == "a"
    assert next(gen) == "b"
    assert next(gen) == "c"
    with pytest.raises(StopIteration):
        next(gen)
