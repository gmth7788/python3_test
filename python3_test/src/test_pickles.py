#!/usr/bin/evn python3
#coding=utf-8

import os
import pickle
import gzip

import FuzzleBool

def export_pickle(self, filename, compress=False):
    fh = None
    try:
        if compress:
            fh = gzip.open(filename, "wb")
        else:
            fh = open(filenname, "wb")
        pickle.dump(self, pickle.HIGHEST_PROTOCOL)
        return True
    except(EnvironmentError, pickle.PickleError) as err:
        print("{0}:export error:{1}".format(os.path.basename("./"),
                                            err))
        return False
    finally:
        if fh is not None:
            fh.close()

def main():
    fb = FuzzleBool.FuzzleBool(0.6)
    export_pickle(fb, r"E:\wbin\python\workspace\a.bin")
    
    print("adsfa")



if __name__ == '__main__':
    main()
    