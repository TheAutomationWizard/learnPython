from abc import ABC, abstractmethod


class abstract_class(ABC):
    @abstractmethod
    def first_abstract_method(self):
        print('This is an abstract method.')


try:
    abstract_object = abstract_class()
    raise Exception('\nPython allows instantiation on abstract class.')
except Exception as error:
    print("We shouldn't be able to create an object, as\n", error)


class abs_class(ABC):
    @abstractmethod
    def first_abstract_method(self):
        print('This is an abstract method.')


class child_abstract_class(abs_class):
    def concrete_method(self):
        print('Hi! I am a concrete method.')

    def first_abstract_method(self):
        print('This is implmentation of first abstract method.')


c = child_abstract_class()
c.concrete_method()

# ***********************************************************
# ***********************************************************
#   Points related to "Abstract Classes" in python
# ***********************************************************


"""

***** Abstract Classes *******
(1) Abstract Classes -> Can't be instantiated.
(2) Class inheriting an Abstract class, must implement abstract methods in order to be instantiable.
(3) Class inheriting an Abstract class, if doesn't implement abstract methods can't be instantiated. 

***** Abstract Methods ******
(4) Abstract Methods can have implementation within abstract classes.
(5) Abstract Methods of Abstract classes can be called from inheriting classes, using super()

"""