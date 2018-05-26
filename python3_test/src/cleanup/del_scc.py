#!/usr/bin/evn python3

import os
from cleanup import convert_sep
from cleanup import del_subtree

def del_scc(path):
    '''To delete .scc generated at checking out in VSS.
    
    path - path string
    
    >>>del_scc('E:/vm_share/aa')
    '''
    for dirpath, dirnames, filenames in os.walk(path):
        dirpath = convert_sep(dirpath, '/', '\\') + '\\'
        files = [x for x in filenames if '.scc' in x]
        for x in files:
            del_subtree(dirpath + x)
    if (os.system('dir /s ' + path+ ' *.scc')): 
        print('Delete recursively .scc file from ' + path + ',successfully.') # not found .scc
    else:
        print('Delete recursively .scc file from ' + path + ',failed.')
        