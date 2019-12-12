class ClassA(object):
    def __new__(cls):
        print(cls.__dict__)
"""
{'__dict__': <attribute '__dict__' of 'ClassA' objects>, '__module__': '__main__', '__weakref__': 
<attribute '__weakref__' of 'ClassA' objects>, '__new__': <staticmethod object at 0x0000000002836CD8>, '__doc__': None}
"""

s = ClassA()

class Employee(object):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __new__(cls, name, salary):
        if 0<salary<10000:
            return object.__new__(cls)
        else:
            return None

    def __str__(self):
        return '{0}({1})'.format(self.__class__.__name__,self.__dict__)

