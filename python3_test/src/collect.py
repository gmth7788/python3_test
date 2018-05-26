#!/usr/bin/evn python3


import math
import collections

#########################
# 搴忓垪绫诲瀷(sequence type)
#########################

#
# tuple
#
t = tuple()  #empty tuple, ()
print("empty tuple is '",t,"'")


#    t[-5]   t[-4] t[-3] t[-2] t[-1]
t = ('venus', 14, 11.76, 'ok', 14)
#    t[0]    t[1]  t[2]   t[3] t[4]
print("tuple is", t)
print("'14'鍑虹幇浜唟0}娆°�".format(t.count(14)))
try:
    print("14鏄{0}涓厓绱犮�".format(t.index(14)))
    print("20鏄{0}涓厓绱犮�".format(t.index(20)))
except ValueError as err:
    print(err)

print(t*2) #replication
t1 = ('another', 'one')
t += t1 #concatenation
print(t)
print(t[:3]) #slice

if ('ok' in t): # in operator
    print("ok is exist.")
else:
    print("ok is not exist.")
    
if (11.765 not in t):    
    print("11.765 is not exist.")
else:
    print("11.765 is exist.")

things = (1, -7.5, ("pea", (5, "Xyz"), "queue")) #tuple宓屽
print('things[2][1][1][2] of (1, -7.5, ("pea", (5, "Xyz"), "queue")) is '+things[2][1][1][2])

(a,b) = ('a', 'b')  #swap value
print((b,a))

for x, y in ((-3, 4), (5, 12), (28, -45)):
    print(math.hypot(x, y))
    
 
#
# name tuple
# OO浼氭洿寮哄ぇ锛屽繕鎺夎繖涓笢涓滃惂銆�
#
Sale = collections.namedtuple("Sale","productid customerid date quantity price")
sales = []
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))
print(sales)

total = 0
for sale in sales:
    total += sale.quantity * sale.price
    print("Total ${0:.2f}".format(total)) # prints: Total $42.46

Aircraft = collections.namedtuple("Aircraft",
                                  "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
print("{0} {1}".format(aircraft.manufacturer, aircraft.model))
print("{0.manufacturer} {0.model}".format(aircraft)) #閫傚簲鎬ф洿寮�
print(aircraft.seating.maximum)

# tuple鐨刾rivate鏂规硶锛歘asdict()锛岃繑鍥炴槧灏勭殑key-value
print("{manufacturer} {model}".format(**aircraft._asdict()))
print("{manufacturer} {model} {seating} ".format(**aircraft._asdict()))

#
# list
# tuple浣跨敤鐨勬柟娉曞叏閮介�鐢ㄤ簬list
#
l = list()  #empty list, []
print("empty list is '",l,"'") 

l = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7]
print(l)
l[1] += 'meters'  #淇敼list涓殑鍏冪礌
print(l)

# 鏄熸爣鍙傛暟涓庝箻绉鍙风殑鍖哄垎
first, *rest = [9, 2, -4, 8, 7] # '*', sequence unpacking operator
print(first, rest)
first, *mid, last = "Charles Philip Arthur George Windsor".split()
print(first, mid, last)
*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories, executable)

def product(a, b, c):
    return a * b * c # here, * is the multiplication operator
print(product(2, 3, 5))
L = [2, 3, 5]
print(product(*L)) # 鏄熸爣鍙傛暟锛坰tarred arguments锛�
print(product(2, *L[1:]))

for i in range(len(L)):  #閬嶅巻閾捐〃锛屼慨鏀瑰悇涓厓绱�
    L[i] = L[i] * 2 -1
print(L)

# list鐨勬墿鍏�
woods = ["Cedar", "Yew", "Fir"]
woods += ["Kauri", "Larch"]
woods.extend(['Pine','Pineapple'])
woods.append('coconut') #鍦╨ist鏈熬娣诲姞涓�釜鍏冪礌
woods.insert(2, 'jujube') #灏嗗厓绱犳坊鍔犲埌list涓紝浣滀负绗�涓厓绱�
woods[2:2] = ['chinese jujube'] #鍚宨nsert
print(woods)

# list鐨勬浛鎹�
woods[1] += 'aa'
woods[1:3] = ['a','b','c']
print(woods)

# list鐨勫垹闄�
woods.pop() #鍒犻櫎list鐨勬渶鍚庝竴涓厓绱�
del woods[2:4] #鍒犻櫎绗�鑷崇3涓厓绱狅紝宸﹂棴鍙冲紑锛孾2,4)
woods[2:4] = [] #鍚屼笂
woods.remove('a')
print(woods)

# 鎺掑簭
woods.reverse() #鍙嶅簭
print(woods)
woods.sort(key=str.lower) #鎸夌収灏忓啓瀛楁瘝鎺掑簭
print(woods)

# list澶ч噺鏁版嵁鐨勫鐞� list comprehensions
# generator鏄痩ist comprehensions鐨勬浛浠ｇ墿锛屾洿寮哄ぇ銆�
leaps = []
for year in range(1980, 2020): #[1980,2020)锛屽乏闂彸寮�
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leaps.append(year)    
print('闂板勾鏈夛細'+str(leaps)) # 璁＄畻闂板勾
leaps = [y for y in range(1980,2020) 
         if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]
print('闂板勾鏈夛細'+str(leaps)) # 璁＄畻闂板勾鐨勭畝娲佸疄鐜�

codes = []
for sex in "MF": # Male, Female
    for size in "SMLX": # Small, Medium, Large, eXtra large
        if sex == "F" and size == "X":
            continue
        for color in "BGW": # Black, Gray, White
            codes.append(sex + size + color)
print(codes) #浜х敓21绉嶇粍鍚�
codes = [s+z+c for s in 'MF' for z in 'SMLX' for c in 'BGW' 
         if not (s == 'F' and z == 'X')]
print(codes) #21绉嶇粍鍚堢殑绠�磥浜х敓鏂瑰紡


#########################
# 闆嗗悎绫诲瀷(set type)
#########################
s = set() #empty set
print(s)
s = {7, "veil", 0, -29, ("x", 11), "sun", frozenset({8, 4, 7}), 913}
print(s)

files = {'a.h', 'a1.htm', '232', 'baa.html'}
html = {x for x in files if x.lower().endswith((".htm", ".html"))} # set comprehension
print(html)


#
# collection - 鑱氶泦
# set - 闆嗗悎
#









