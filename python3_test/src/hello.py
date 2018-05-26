#!/usr/bin/evn python3

import math
import unicodedata

print('Hello','world!')

for _ in (0, 1, 2, 3, 4, 5):
    print("Hello")


print(round(1.9385, 2))
print(round(13579,-3))
print(round(13479,-3))
print(round(38.4,-1))
print(round(31.7,-1))

x = 2.75
print(x.as_integer_ratio())
print(math.modf(x))


text = """A triple quoted string like this can include 'quotes' and
"quotes" without formality. We can also escape newlines \
so this particular string is actually only two lines long."""
print(text)

s = ("This is the nice way to join two long strings "
"together; it relies on string literal concatenation.")

s = ("abcdccef")
print(s.center(10))
print(s.count('c'))


table = "".maketrans("\N{bengali digit zero}"
         "\N{bengali digit one}\N{bengali digit two}"
         "\N{bengali digit three}\N{bengali digit four}"
         "\N{bengali digit five}\N{bengali digit six}"
         "\N{bengali digit seven}\N{bengali digit eight}"
         "\N{bengali digit nine}", "0123456789")
print("20749".translate(table)) # prints: 20749
print("\N{bengali digit two}07\N{bengali digit four}"
      "\N{bengali digit nine}".translate(table)) # prints: 20749





print(chr(8734))
print(unicodedata.normalize("NFKC",chr(0x85c3)) )



# dynamic typing

route = 866
print(route, type(route))

route = "North"
print(route, type(route))

while True:
    print("a")
    if True:
        break
    print('b')
print('c')
    
    
#
# function and call
#    
def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)

age = get_int("enter your age: ")
print(age)
    

#
# sum1.py
#
print("Type integers, each followed by Enter; or ^D or ^Z to finish")
total = 0
count = 0
while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
            total += number
            count += 1
        except ValueError as err:
            print(err)
            continue
        except EOFError:
            break
    else:
        break
    if count:
        print("count =", count, "total =", total, "mean =", total / count)





