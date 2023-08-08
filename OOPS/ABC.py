'''
Abstract Base Class ABC
An abstract class can be considered as a blueprint for other classes.
It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
'''
from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
class Rectangle(shape):
    
    def area(self):
        print("In rectangle")

class trinagle(shape):
    var = 5

rec = Rectangle()
rec.area()

