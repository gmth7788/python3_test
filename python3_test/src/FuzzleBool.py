#!/usr/bin/evn python3
#coding=utf-8

class FuzzleBool():
    '''
    继承自object，创建一个完整的数据类型
    '''
    def __init__(self, value):
        '''
        FuzzleBool是固定的，不允许存取属性。
                      因此将__value定义为私有属性
        '''
        self.__value = value if 0.0 <= value <= 1.0 else 0.0
        
    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__, self.__value)
    
    def __str__(self):
        return str(self.__value)
        
    #
    # 基本逻辑运算符（与、或、非和异或，&, |, ~, ^）
    #
    def __and__(self, other):
        '''
        x&y
        
        [注]y&x
        大多数二元运算符，都同时具备“i”（in-place）和“r”（反射，即互换操作数）。
        因此该方法不必要。
        '''
        return FuzzleBool(min(self.__value, other.__value))
    
    def __iand__(self, other):
        '''
        x&=y
        '''
        self.__value = min(self.__value, other.__value)
        return self
    
    def __or__(self, other):
        '''
        x|y
        '''
        return FuzzleBool(max(self.__value, other.__value))
    
    def __ior__(self, other):
        '''
        x|=y
        '''
        self.__value = max(self.__value, other.__value)
        return self

    def __invert__(self):
        '''
        ~x
        '''
        return FuzzleBool(1.0 - self.__value)
    
    #
    # FuzzleBool类型与bool,int,float,str等数据类型的转换功能
    #
    def __bool__(self):
        return self.__value > 0.5
    
    def __int__(self):
        return round(self.__value)
    
    def __float__(self):
        return self.__value
    
    #
    # 支持比较操作符全集（<, <=, ==, !=, >=, >）
    # 【注】至少实现其中3种方法，python可以从<推导出>，从==推导出!=，从<=推导出>=。
    #
    def __lt__(self, other):
        return self.__value < other.__value
    
    def __le__(self, other):
        return self.__value <= other.__value
        
    def __eq__(self, other):
        return self.__value == other.__value
        
    #
    # 默认情况下，自定义类型支持“==”操作符（总返回False），并且是可哈希运算的。
    # 因此可以作为字典的键，可以加入到集合中。
    # 但若重载了__eq__()方法，提供了正确的相等性测试功能，实例就不再是可哈希运算的。
    # 为了弥补，重载__hash__()方法。
    # 【注意】对象的哈希值，必须保持不变。因此利用对象独一无二的ID计算哈希值。
    # id()，返回对象在内存中的地址。is操作符就是利用id()确定两个对象引用是否指向相同的对象。
    #
    def __hash__(self):
        return hash(id(self))
    
    #
    # 支持str.format()格式规约
    # 所有内置类都包含适当的__format__()方法，这里使用float.__format__()方法。
    #
    def __format__(self, format_spec):
        return format(self.value, format_spec)
    #    return self.__value.__format__(format_spec)
    
    #
    # 结合操作，conjunction
    # fa = FuzzleBool(0.23)
    # fb = FuzzleBool(0.85)
    # fc = FuzzleBool(0.69)
    # fconj = FuzzleBool.conjunction(fa,fb,fc)的效率胜过(fa & fb & fc)
    # 每个&都又一次函数调用
    # 
    @staticmethod
    def conjunction(*fuzzles):
        return FuzzleBool(min([float(x) for x in fuzzles]))
    
    #
    # 析取操作，disjunction
    # fa = FuzzleBool(0.23)
    # fb = FuzzleBool(0.85)
    # fc = FuzzleBool(0.69)
    # fdisj = FuzzleBool.disjunction(fa,fb,fc)的效率胜过(fa | fb | fc)
    # 每个&都又一次函数调用
    # 
    @staticmethod
    def disjunction(*fuzzles):
        return FuzzleBool(max([float(x) for x in fuzzles]))        
    

if __name__ == '__main__':
    a = FuzzleBool(0.75)
    print(repr(a))
    b = eval(repr(a))
    print(b)
    
    fa = FuzzleBool(0.23)
    fb = FuzzleBool(0.85)
    fc = FuzzleBool(0.69)
    fconj = FuzzleBool.conjunction(fa,fb,fc)
    print(fconj)
    print(fa & fb & fc)
    fdisj = FuzzleBool.disjunction(fa,fb,fc)
    print(fdisj)
    print(fa | fb | fc)
