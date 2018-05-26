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


def build_lib(path, ext, libname):
    '''build 'libname' library from object files which have 'ext' extension name.
     
    path     - path string
    ext      - extension file name of object file
    libname  - library file name
    
    >>>build_lib('E:/vm_share/aa/a', '.doc', 'a.lib')
    '''
    obj_str = ''
    obj_names = ''
    flag = False
    cmd = ''
    fh = None
    try:
        fh = open('build_lib.bat', "w", encoding="utf8")
        for dirpath, dirnames, filenames in os.walk(path):
            dirpath = convert_sep(dirpath, '/', '\\')
            obj_names = [x for x in filenames if x.endswith(ext)]
            for i in obj_names:
                obj_str = dirpath + '\\' + i + ' '
                if (not flag):
                    cmd = 'i386-elf-ar.exe -crus ' + libname + ' ' +  obj_str
                    flag = True
                else:
                    cmd = 'i386-elf-ar.exe -r ' + libname + ' ' +  obj_str
                fh.write(cmd+'\n')
    except EnvironmentError as err:
            print(err)
    finally:
        if fh is not None:
            fh.close()
#            os.system('build_lib.bat')
        


build_lib('C:/SZIDE_SAT/workspace/szos_mis_x86/SAT_X86_Debug', '.o', './szos_sat_x86.lib')

