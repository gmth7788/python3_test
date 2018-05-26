#!/usr/bin/evn python3

import os
from cleanup import convert_sep

def del_subtree(path):
    '''delete a subtree

    path - path string
    
    >>>del_subtree('E:/vm_share/aa')
    '''
    for dirpath, dirnames, filenames in os.walk(path,False): # directories are generated bottom-up
        dirpath = convert_sep(dirpath, '/', '\\') + '\\'
        for x in filenames:
            cmd = 'DEL /Q /F ' + dirpath + x
            os.system(cmd)
        if (os.path.isdir(dirpath)):
            os.rmdir(dirpath)
            
            