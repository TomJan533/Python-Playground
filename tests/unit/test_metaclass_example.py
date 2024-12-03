from src.metaclass_example import MyClass, get_custom_attribute


def test_metaclass_adds_custom_attribute():
    """
    Test that the metaclass adds a custom attribute to the class.
    """
    assert hasattr(MyClass, 'custom_attribute'), "MyClass should have 'custom_attribute'"
    assert MyClass.custom_attribute == "Created by Meta"


def test_get_custom_attribute():
    """
    Test the function that retrieves the custom attribute.
    """
    result = get_custom_attribute()
    assert result == "Created by Meta"
