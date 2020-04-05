#!/usr/bin/python

class Test:
    def __init__(self):
        self._a = 1
        self._b = '2'
        return

    def get_a(self):
        return self._a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, val):
        self._a = int(val)

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, val):
        self._b = str(val)

class Test2:
    def __init__(self):
        self._a = 1
        self._b = 2

    def get_a(self):
        return self._a

    def set_a(self, val):
        self._a = int(val)

    def get_b(self):
        return self._b

    def set_b(self, val):
        self._b = str(val)

test = Test()
test2 = Test2()
print(test.a)
print(test.b)

print()

print(test2.get_a())
print(test2.get_b())

print()

test.a = 3
print(test.a)
