#!/usr/bin/evn python3

import argparse
from cleanup import del_subtree


def main():
    parser = argparse.ArgumentParser(description='Delete tree.',
                                    add_help=True)
    parser.add_argument('-p', dest='path', action='store',
                    help='assign the root of the subtree to be deleted')
    args = parser.parse_args()
    
    del_subtree(args.path)
    
    print('ternmate normally.')

if __name__ == '__main__':
    main()
