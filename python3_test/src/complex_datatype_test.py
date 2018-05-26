#!/usr/bin/python
#coding=utf-8


instr_col = []

class instr_warp:
    fun_name = ""        #函数名
    call_times = 0       #调用次数
    instr_num = 0        #指令数

    def set_fun_name(self, name):
        self.fun_name = name
    
    def incr_call_times(self, times):
        self.call_times += times
        
    def set_instr_num(self, num):
        self.instr_num += num

    def disp(self):
        print("******************")
        print(self.fun_name)
        print(self.call_times)
        print(self.instr_num)
        print("******************")

def calc_instr():
    for i in range(10):
        instr = instr_warp()
        instr.set_fun_name("fun"+str(i))
        instr.incr_call_times(i)
        instr.set_instr_num(100 + i * 10)
        instr_col.append(instr)
    
def extract_from_tag(tag, line):
    opener = "<"+tag+">"
    closer = "</"+tag+">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None
        
        
if __name__ == '__main__':
#    calc_instr()
#    
#    for i in instr_col:
#        i.disp()

#    ret = extract_from_tag("info", '''
#    sadfasdf<info>的房间爱思
#    考附件</info>fasldkf
#    jasdlfjkasdf 343245jkjkasd''')
#    print(ret)

    table="".maketrans("\N{bengali digit zero}"
                       "\N{bengali digit one}"
                       "\N{bengali digit two}"
                       "\N{bengali digit three}"
                       "\N{bengali digit four}"
                       "\N{bengali digit five}"
                       "\N{bengali digit six}"
                       "\N{bengali digit seven}"
                       "\N{bengali digit eight}"
                       "\N{bengali digit nine}",
                       "0123456789")
    print("\N{bengali digit nine}"
          "\N{bengali digit three}"
          "\N{bengali digit one}"
          "\N{bengali digit four}"
          "\N{bengali digit three}"
          .translate(table))
    

    table="".maketrans("0123456789",
                       "甲乙丙丁戊己庚辛壬癸")
    print("45784"
          .translate(table))
        
    table="".maketrans("甲乙丙丁戊己庚辛壬癸",
                       "0123456789")
    print("戊丙"
          .translate(table))
    
    "".maketrans()
    
    


