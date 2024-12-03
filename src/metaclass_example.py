"""
Metaclasses in Python are classes of classes that define how classes behave.
They allow you to customize class creation by overriding methods like __new__ or __init__.
A metaclass is specified using the 'metaclass' keyword in a class definition
and can modify or enforce rules for the attributes and methods of the resulting class.
"""

class Meta(type):
    """A simple metaclass that modifies class behavior.

    Args:
        type (_type_): _description_
    """
    
    def __new__(cls, name, bases, attribute_dict):
        """
        Args:
            cls: The metaclass itself.
            name: The name of the class being created.
            bases: A tuple of base classes for the class being created.
            attribute_dict: A dictionary containing the class's attributes and methods.
        """
        # Add a custom attribute to the class
        attribute_dict['custom_attribute'] = f"Created by {cls.__name__}"
        return super().__new__(cls, name, bases, attribute_dict)
        
        
class MyClass(metaclass=Meta):
    """
    A class using the Meta metaclass.
    """
    pass


def get_custom_attribute():
    """
    Demonstrates metaclass behavior by accessing the custom attribute.
    """
    return MyClass.custom_attribute