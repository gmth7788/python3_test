#!/usr/bin/evn python3

import os
import argparse

def convert_sep(path, old_sep, new_sep):
    '''convert the old separating character to a new one in path string
    
    path     - path string
    old_sep  - the old separating character
    new_sep  - the new separating character
    
    >>>convert_sep('E:/vm_share/aa/arch/i86/os_ext/aa.scc','/','\\')
    'E:\vm_share\aa\arch\i86\os_ext\aa.scc'
    '''
    path = path.replace('\\','/')
    drive,tail = os.path.splitdrive(path)
    dir,filename = os.path.split(tail)
    dir_parts = str(dir).split(old_sep)
    s = ''
    for i in dir_parts:
        if len(i) > 0:
            s += i + new_sep
    s = drive + new_sep + s + filename
    return s 


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


def main():
    parser = argparse.ArgumentParser(description='Delete svn hide directory generated at checking out in SVN.',
                                    add_help=True)
    parser.add_argument('-p', dest='path', action='store',
                    help='assign the root of the subtree to be deleted')
    args = parser.parse_args()
    
    del_svn_hide_dir(args.path)
    
    print('ternmate normally.')

if __name__ == '__main__':
    main()





