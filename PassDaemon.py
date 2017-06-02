#!/usr/bin/env python
'''A program that automatic fills credential base on actions monitored.


'''

import sys
import pickle
import argparse
import binascii
import keyboard
from ops_storage import *
from ops_crypto import CryptoCapabilities
from ops_hook import hook_init
from ops_cred import new_cred


__author__ = "Mr.Kua"
__copyright__ = "Copyright 2017, the IPD Project"
__license__ = "GPL"
__email__ = "nanifold@gmail.com"



if __name__ == "__main__":
    CryptoManager = CryptoCapabilities()

    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--create", type=str, help="mnemonic for this sequence.")
    args = parser.parse_args()

    try:
        if args.create:
            print "please input mnemonic:"
            mnemonic = args.create
            new_cred(mnemonic, CryptoManager)     # create vault for credentity
            print "Done.."
            sys.exit(0)
        else:
            hook_init(CryptoManager)
    except KeyboardInterrupt:
        print "Graceful Exiting.."
        sys.exit(0)