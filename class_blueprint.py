#!/usr/bin/env python3
# self educate here https://www.youtube.com/watch?v=fmqkncV6JIY
"""Line 1 doc string: shebang line. This above line is optional"""

import abc
"""Line 4: The next line after shebang are the import statements. These are always on the top"""


class CamelCaseConvention:
    # self educate here on topic https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
    """Syntax: class ClassName. Class-name follows CamelCase naming Convention  """
    variable = "I'm class variable"
    #  self educate here https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2
    """class variables/ attributes can be accessed by cls.variable(class method)/ self.variable(Instance method)"""

    # use it to instantiate or create/store class object. This is the first method of a class.
    def __init__(self, name, age):
        """It is a Initializer/ Constructor/ Instance method. self is first parameter passed to the instance method.
        Methods name is defaulted to __init__"""
        self.name = name
        self.no_of_years = age
        """Instance attributes can be accessed through out the class by using self.attribute_name"""

    # use this when you need access to variables or methods in class
    def print_attributes(self):
        """Instance method. self is the only way to gain access to variables or methods in class"""
        print("\nInstance Method: \nI'm {} at age {}".format(self.name, self.no_of_years))
        return self.variable

    # use this when method is related to class but don't require access to variables or methods in class
    @staticmethod
    def no_access_to_class(gender):
        """Static method, declare it using decorator @staticmethod on top of the method name"""
        print("\nStatic Method: \nI can't access the data in class")
        return gender

    # use it only when you need to manipulate the class
    # self educate here https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
    @classmethod
    def manipulate_class(cls, name, age):
        """Class method's first parameter is cls"""
        print('\nFiring class method...')
        cls.variable = "I'm modified in class method"
        return cls(name, age)

    # use it when you want to declare a mandatory method with implementation in sub-class
    # self educate here https://www.youtube.com/watch?v=UDmJGvM-OUw
    @abc.abstractmethod
    def mandatory_subclass_method(self):
        """Implemented in subclass/ Inherited class"""
        pass


# Inheritance to show abstract method implementation
# self educate here on topic https://www.youtube.com/watch?v=RSl87lqOXDE
class InheritingMainClass(CamelCaseConvention):
    """Syntax: class ClassName(Inheriting ClassName)"""
    def __init__(self, name, age, living_at):
        """super keyword is used to refer to main class (recommended) or alternatively you can use the ClassName that
        you are inheriting (ex: CamelCaseConvention.__init__(self, name, age))"""
        super().__init__(name, age)
        self.city = living_at

    def mandatory_subclass_method(self):
        print("\n----Executing abstract method----")
        # self.no_access_to_class('M')
        # self.print_attributes()
        return f"I'm {self.name} residing at {self.city} since {self.no_of_years} years"


if __name__ == '__main__':
    # self educate here https://www.youtube.com/watch?v=sugvnHA7ElY
    """Line 71: Module is only executed as main program"""

    # create a class object to access methods in class. This by default executes __init__ method
    class_object = CamelCaseConvention('John', 21)

    # Line 80: Way to access a Instance method. This doesn't print returned object
    """Requires class object to access it"""
    class_object.print_attributes()
    """To print the object returned by a method use print as in line 83"""
    print("\nPrinting return statement")
    print(class_object.print_attributes())

    # Line 87: Way to access a Static method.
    """Doesn't require class object to access it"""
    print(CamelCaseConvention.no_access_to_class('male'))

    # Line 90: Way to access a class method.
    modified_object = CamelCaseConvention.manipulate_class('Chris', 32)
    """When you print it as you class class attributes are modified"""
    print(modified_object.print_attributes())

    # Line 95: Way to access a abstract method.
    abstract_object = InheritingMainClass('Vamshi', 32, 'California')
    """When you print it as you class class attributes are from abstract object"""
    print(abstract_object.mandatory_subclass_method())
