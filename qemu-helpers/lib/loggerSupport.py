#!/usr/bin/env python

import sys,os
#TODO IMPORT UITLS

DEBUG=True
VERBOSE=True

def fail(msg):
    print("[F] %s" % msg)
    sys.exit(42)

def debug(msg):
    if DEBUG:
        print("[D] %s" % (msg))

def debug_pause(msg):
    debug(msg)
    input("<press enter to roll forward>")

def verbose(msg):
    if VERBOSE:
        print("[V] %s" % (msg))

def info(msg):
    print("[*] %s" % (msg))

def cleanup(msg):
    print("TODO delete(rm -v $OPTBUILDDIR)")

    #if [ "$ARCH" != "" ] && [ -d $OPTGCCARCH ]
    #then
        #ls $OPTGCCARCH | grep -v host | xargs -i rm -rf $OPTGCCARCH/{}

