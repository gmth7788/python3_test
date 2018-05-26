#!/usr/bin/evn python3

import locale
import decimal
import math
import sys

#########################
# 位置参数(position argument)替换
#########################
print("The novel '{0}' was published in {1}".format("Hard Times", 1854))
print("{{{0}}} {1} ;-}}".format("I'm in braces", "I'm not")) #位置参数中包含{}

#########################
# 关键字参数(keyword argument)替换
# [注]关键字参数总是位于位置参数之后。
#########################
print("The {who} was {0} last week".format(12, who="boy"))

stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
print("We have {0[1]} and {0[2]} in stock".format(stock))


#########################
# 使用命名属性(named attribute)
#########################
print("math.pi=={0.pi} sys.maxunicode=={1.maxunicode}".format(math, sys))



#########################
# 连接字符串和数字的方法
#########################
print("{0}{1}".format("The amount due is $", 200))
print('100'.join('￥ ')) #‘￥100 ’
print(('100'.join('￥ ')).strip()) #‘￥100’


#########################
# 使用字典(dict)
#########################
d = dict(animal="elephant", weight=12000)
print("The {0[animal]} weighs {0[weight]}kg".format(d)) #同时显示key-value pair。

#########################
# 映射解包(mapping unpacking)
# **，将映射（如字典）解包为
# key-value列表。
# [注]locals()内置函数返回一个字典，
# key为局部变量名，value为局部变量的值。
# [注]**为“映射解包运算符”(mapping unpacking operator)，
# 映射解包后产生一个key-value列表。
# [注]**只用于format() 
#########################
element = "Silver"
number = 47
print("Element {number} is {element}".format(**locals()))
print(locals())
print("Element {0[number]} is {0[element]}".format(locals()))



#########################
#decimal.Decimal
#########################
decimal.Decimal("3.4084") #decimal.Decimal的表现形式(representation form)
                          #"表现形式"提供一个字符串，python可由此重新创建所表示的对象。
print(decimal.Decimal("3.4084")) #decimal.Decimal的字符串形式
                          #"字符串形式"目的在于方便人们阅读。


#########################
#字符形式(string form) vs. 表现形式(representation form)
#由“转换标识符(conversion specifier)”指定：
#   s - 字符形式
#   r - 表现形式
#   a - 表现形式，但使用ASCII字符
#########################
print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("93.4")))
print("{0} {0!s} {0!r} {0!a}".format('王彬'))
print(chr(0x738b)+chr(0x5f6c))


#########################
# 格式化输出(format specifications)
# 通用格式：
#   :填充字符(fill)，除'}'以外的所有字符
#    对齐方式(align)，< 左对齐
#                   > 右对齐
#                   ^ 中间对齐
#                   =pad，符号与数字间字符的数量
#    符号方式(sign)，+ 强制有符号
#                   - 只有负数才需要符号
#    #数制前缀， 0b,0o,0x
#    填充0的数量
#    宽度(width)，最小域宽度
#    ，用于分组
#    .精度(precision)，字符串的最大宽度，浮点数位数
#    类型(type)，整型：b,c,d,n,o,x,X
#               浮点型：e,E,f,g,G,n,%
#########################

# 格式化字符串
s = "The sword of truth"
print("{0}".format(s)) # default formatting
print("{0:25}".format(s)) # minimum width 25

print("{0:<25}".format(s)) # left align, minimum width 25
print("{0:>25}".format(s)) # right align, minimum width 25
print("{0:^25}".format(s)) # center align, minimum width 25

print("{0:-<25}".format(s)) # - fill, left align, minimum width 25
print("{0:.>25}".format(s)) # . fill, right align, minimum width 25
print("{0:^25.10}".format(s)) # center align, maximum width 10
print("{0:.10}".format(s)) # maximum width 10


# 格式化整型
# 在符号与数字之间用0填充
print("{0:0=12}".format(8749203)) # 0 fill, minimum width 12
print("{0:0=12}".format(-8749203)) # 0 fill, minimum width 12
# 最小宽度12,0占位（pad）
print("{0:012}".format(8749203)) # 0 fill, minimum width 12
print("{0:012}".format(-8749203)) # 0 fill, minimum width 12
# 用*填充，最小宽度15
print("{0:*<15}".format(18340427)) # * fill, left align, min width 15
print("{0:*>15}".format(18340427)) # * fill, right align, min width 15
print("{0:*^15}".format(18340427)) # * fill, center align, min width 15
print("{0:*^15}".format(-18340427)) # * fill, left align, min width 15
# 符号
print("[{0: }] [{1: }]".format(539802, -539802))  # space or - sign
print("[{0:+}] [{1:+}]".format(539802, -539802))  # force sign
print("[{0:-}] [{1:-}]".format(539802, -539802))  # - sign if needed
# 数制类型
print("{0:b} {0:o} {0:x} {0:X}".format(14613198))
print("{0:#b} {0:#o} {0:#x} {0:#X}".format(14613198))
# 整型数分组
print("{0:,} {0:*>13,}".format(int(2.39432185e6)))

# n - 对于整型类似于d，对于浮点型类似于g
# 但其特殊性体现在，使用本地小数分隔符和分组分隔符
loc = locale.getlocale() # get current locale
locale.setlocale(locale.LC_ALL, "")  #python检验LANG环境变量决定用户的local信息
x, y = (1234567890, 1234.56)
print("{0:n} {1:n}".format(x, y))
locale.setlocale(locale.LC_ALL, "C") #C,小数分隔符和分组分隔符为空
print("{0:n} {1:n}".format(x, y))
#locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
#print("{0:n} {1:n}".format(x, y))
locale.setlocale(locale.LC_ALL, loc) # restore saved locale


# 格式化浮点数
amount = (10 ** 3) * math.pi
print("[{0:12.2e}] [{0:12.2f}]".format(amount))
print("[{0:*>12.2e}] [{0:*>12.2f}]".format(amount))
print("[{0:*>+12.2e}] [{0:*>+12.2f}]".format(amount))
print("{:,.6f}".format(decimal.Decimal("1234567890.1234567890")))
print("{:,.6g}".format(decimal.Decimal("1234567890.1234567890")))

# 格式化虚数
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917+1.2042j))
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917-1.2042j))
print("{:,.4f}".format(3.59284e6-8.984327843e6j))
