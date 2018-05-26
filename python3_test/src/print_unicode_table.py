#!/usr/bin/evn python3
#coding=utf-8

import sys
import unicodedata

def print_unicode_table(word):
    print("decimal   hex  chr {0:^40}".format("name"))
    print("------ ----- ---  {0:-<40}".format(""))
    
    code = ord(" ")
    end = sys.maxunicode
    
    try:
        while code < end:
            c = chr(code)
            name = unicodedata.name(c, "***unknown code***")
            if word is None or word in name.lower():
                print("{0:7}{0:5X} {0:^3c} {1}".format(code, name.title()))
                
            code += 1
    except UnicodeEncodeError:
        print("发生异常：UnicodeEncodeError。程序退出。")
        return None
        
        
if __name__ == '__main__':  
    print_unicode_table(None)       
    
