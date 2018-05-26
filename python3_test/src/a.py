#!/usr/bin/python
#coding=utf8

import random
import copy
import math

BZ2_AVAILABLE = True
try:
    import bz2
    print("import successfully.")
except ImportError:
    BZ2_AVAILABLE = False
    print("import failed")


forenames=[]
surnames=[]
names=[]
f_forenames=open("e:/wbin/rub/data/forenames.txt", encoding="utf8")
f_surnames=open("e:/wbin/rub/data/surnames.txt", encoding="utf8")

for index, item in enumerate(f_forenames, start=1):
    forenames.append(item.rstrip())

for index, item in enumerate(f_surnames, start=1):
    surnames.append(item.rstrip())

f_forenames.close()
f_surnames.close()

print(forenames)
print(surnames)

fh = open("e:/wbin/rub/data/names.txt", "w", encoding="utf8")

name=[]
for forename in forenames:
    for surname in surnames:
        name.append(forename+surname)
print(name)
print(len(name))
#
#for i in range(6):
#    name = "{0}{1}\n".format(random.choice(forenames),
#                             random.choice(surnames))
#    print(name)
#    fh.write(name)



class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)
    
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)
        
class Circle(Point):
    def __init__(self, radius, x = 0, y = 0):
        super().__init__(x,y)
        self.radius = radius
        
    def __eq__(self, other):
        return self.radius == other.radius and \
             self.x == other.x and \
             self.y == other.y
    
    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)
    
    def __str__(self):
        return self.repr(self)        

    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        assert radius > 0, "园的半径应当大于0"
        self.__radius = radius
        
        
        
a = Point()
print(repr(a))
b = Point(3,4)
print(repr(b))
print(a == b)

p = Point(3,9)
print(repr(p))
q = eval(repr(p))
print(repr(q))
print(p == q)

print(p)
        
copy_a = copy.copy(a)
print(copy_a)      
print(a == copy_a)  

circle = Circle(6, 4, 6)
print(circle.area)
circle.radius = 2
print(circle.area)
circle.radius = -2




