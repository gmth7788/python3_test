#!/usr/bin/evn python3
#coding=utf-8

from tkinter import *

root = Tk()

Button(root, text="A").pack(side=LEFT, expand=NO, fill=BOTH,padx=10)
Button(root, text="B").pack(side=TOP, expand=YES, fill=BOTH)
Button(root, text="C").pack(side=RIGHT, expand=YES, fill=NONE,
                            anchor=NE)
Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y)
Button(root, text="E").pack(side=TOP, expand=NO, fill=BOTH)
Button(root, text="F").pack(side=BOTTOM, expand=YES, fill=Y)
Button(root, text="G").pack(anchor=SE)

#禁止窗口resize
#root.resizable(0,0)


root.mainloop()

    

