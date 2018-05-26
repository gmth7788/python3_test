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
	drive,tail = os.path.splitdrive(path)
	dir,filename = os.path.split(tail)
	dir_parts = str(dir).split(old_sep)
	s = ''
	for i in dir_parts:
		if len(i) > 0:
			s += i + new_sep
	s = drive + new_sep + s + filename
	return s 

def del_scc(path):
	'''To delete .scc generated at checking out in VSS.
	
	path - path string
	
	>>>del_scc('E:/vm_share/aa')
	'''
	for dirpath, dirnames, filenames in os.walk(path):
		dirpath = convert_sep(dirpath, '/', '\\') + '\\'
		files = [x for x in filenames if '.scc' in x]
		for x in files:
			cmd = 'DEL /Q /F ' + dirpath + x  # DEL /Q /F /S , ok!
			print(cmd)
			os.system(cmd)
	if (os.system('dir /s ' + path+ ' *.scc')): 
		print('Delete recursively .scc file from ' + path + ',successfully.') # not found .scc
	else:
		print('Delete recursively .scc file from ' + path + ',failed.')
			
			
def main():
	parser = argparse.ArgumentParser(description='To delete .scc generated at checking out in VSS.',
									add_help=True)
	parser.add_argument('-p', dest='path', action='store',
					help='assign the root of the subtree to be deleted')
	args = parser.parse_args()
	
	del_scc(args.path)

if __name__ == '__main__':
	main()




