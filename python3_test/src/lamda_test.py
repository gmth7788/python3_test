#!/usr/bin/env python3


# lamda function
s = lambda x: " " if x == 1 else "s"

a = 121
print('{0}'.format(s(a)))
a = 1
print('{0}'.format(s(a)))

# key function for built-in sorted()
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(elements)
elements.sort(key=None, reverse=False)
print(elements)
elements.sort(key=lambda x: x[2], reverse=False) # sort as string
print(elements)
elements.sort(key=lambda x: (x[0], x[2]), reverse=True)
print(elements)

