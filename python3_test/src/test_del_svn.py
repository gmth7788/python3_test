#!/usr/bin/evn python3

import argparse
from cleanup import del_svn_hide_dir


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


