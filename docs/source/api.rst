"""
Module: pythontemplate
=====================

This module provides a template for building Python applications. It includes
a variety of classes and functions that can be used to structure and organize
your code.

Classes
-------

.. autoclass:: MyClass
   :members:
   :undoc-members:
   :inherited-members:
   :special-members: __init__

   This class is an example of how to define a custom class in Python. It
   includes several methods that demonstrate common patterns for object-
   oriented programming.

Functions
---------

.. autofunction:: my_function
   :noindex:

   This function is an example of how to define a standalone function in
   Python. It takes two arguments and returns their sum.

"""

class MyClass:
    """
    A simple example class.

    Attributes:
        attr1 (int): The first attribute.
        attr2 (str): The second attribute.

    """

    def __init__(self, attr1: int, attr2: str):
        """
        Initialize the object with the given attributes.

        Args:
            attr1 (int): The first attribute.
            attr2 (str): The second attribute.

        """
        self.attr1 = attr1
        self.attr2 = attr2

    def method1(self, arg1: int) -> int:
        """
        A simple method that takes an integer argument and returns its double.

        Args:
            arg1 (int): The argument.

        Returns:
            int: The double of the argument.

        """
        return arg1 * 2

def my_function(arg1: int, arg2: str) -> str:
    """
    A simple function that takes an integer and a string and returns their
    concatenation.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
       
