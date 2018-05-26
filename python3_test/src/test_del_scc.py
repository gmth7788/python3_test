#!/usr/bin/evn python3

import argparse
from cleanup import del_scc


def main():
    parser = argparse.ArgumentParser(description='To delete .scc generated at checking out in VSS.',
                                    add_help=True)
    parser.add_argument('-p', dest='path', action='store',
                    help='assign the root of the subtree to be deleted')
    args = parser.parse_args()
    
    del_scc(args.path)

if __name__ == '__main__':
    main()

