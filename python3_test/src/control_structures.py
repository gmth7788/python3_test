#!/usr/bin/evn python3

import sys

#
# if
#
if sys.platform.startswith('win'):
    platform = 'windows'
elif sys.platform.startswith('linux'):
    platform = 'linux'
else:
    platform = 'known'
print(platform)

platform = 'windows' if sys.platform.startswith('win') else 'known' # brief 'if' 
print(platform)

#
# while
#
def list_find(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index

l = ['aad','efs','3ss']
i = list_find(l, '3ss') # found
print(i)
i = list_find(l, 'ok') # not found
print(i)

#
# for
#
def list_find1(lst, target):
    for index, x in enumerate(lst):
        if x == target:
            break
    else:
        index = -1
    return index     

l = ['aad','efs','3ss']
i = list_find1(l, '3ss') # found
print(i)
i = list_find1(l, 'ok') # not found
print(i)        
        

#
# exception
#   except always order from most specific to least specific.
# namely,from lowest in the hierarchy to highest in the hierarchy. 
#
#d=[23,34,4,45,2,99] #ok
d={}   #KeyError
#d=[]    #LookupError
try:
    x = d[5]
except KeyError as e:
    print("Invalid key used", e)
except LookupError as e:
    print("Lookup error occurred", e)
else:
    print(x) # no except raised
finally:
    print('finally') # always executing


def read_data(filename):
    lines = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
    return lines

a = read_data('./hello.py')
print(a)

# raise exception












# sequence unpacking operater vs. mapping unpacking operator
def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print("positional argument {0} = {1}".format(i, arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key, kwargs[key]))

s = [23,23,'daf',3.34]
m = dict(id=211, name='pear', price=4.5)
print_args(*s, **m)





