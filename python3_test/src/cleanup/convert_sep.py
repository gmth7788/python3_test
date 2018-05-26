#!/usr/bin/evn python3

import os

def convert_sep(path, old_sep, new_sep):
    '''convert the old separating character to a new one in path string
    
    path     - path string
    old_sep  - the old separating character
    new_sep  - the new separating character
    
    >>>convert_sep('E:/vm_share/aa/arch/i86/os_ext/aa.scc','/','\\')
    'E:\vm_share\aa\arch\i86\os_ext\aa.scc'
    '''
    drive,tail = os.path.splitdrive(path)
    dir,filename = os.path.split(tail)
    dir_parts = str(dir).split(old_sep)
    s = ''
    for i in dir_parts:
        if len(i) > 0:
            s += i + new_sep
    s = drive + new_sep + s + filename
    return s 
