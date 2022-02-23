#!/usr/bin/env python3 

class betterString(str):
    def __init__(self, str):
            self.str = str
    def __repr__(self):
            return f"{self.__class__.__name__}('{self.str}')"
    def __str__(self):
            return f"{self.str}"
    def __add__(self, other):
            if type(other) is str:
                return self.str +" "+ other
            else:
                return self.str +" "+ str(other)
    def __sub__(self, other):
            if str(other) in self.str:
                return self.str.replace(str(other), '')
            else:
                return None

x = betterString("A thing")
print(repr(x))
print(x + 1)
print(x - 'A ')

