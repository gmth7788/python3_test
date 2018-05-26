#!/usr/bin/evn python3

import os
from cleanup import convert_sep
from cleanup import del_subtree

def del_svn_hide_dir(path):
    '''delete svn hide directory generated at checking out in SVN.

    path - path string
    
    >>>del_svn_hide_dir('E:/vm_share/aa')
    '''
    for dirpath, dirnames, filenames in os.walk(path):
        dirpath = convert_sep(dirpath, '/', '\\') + '\\'
        svn_hide_dir = [x for x in dirnames if '.svn' in x]
        for x in svn_hide_dir:
            del_subtree(dirpath+x)
    if (os.system('dir /s ' + path+ ' *.svn')): 
        print('Delete recursively .svn file from ' + path + ',successfully.') # not found .scc
    else:
        print('Delete recursively .svn file from ' + path + ',failed.')            
            
            