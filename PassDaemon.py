import sys
import pickle
import binascii
import keyboard
from crypto_ops import cryptonomicon
crypto = cryptonomicon()
from storage import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-c","--create", type=str, help="mnemonic for this sequence.")
args = parser.parse_args()


def record_sequence(credentity):
    '''
    store credentity of your choice into registry encrypted.
    '''
    import pickle
    recorded = keyboard.record(until='esc')
    c = pickle.dumps(recorded)
    ciphertext = crypto.encrypt(c)
    addData(credentity, ciphertext)

def __add_abbreviation(source_text, credentity, match_suffix=True, timeout=2):
    '''
    overloaded add_abbreviation(), adding custom callback.
    '''
    cryptdata = getData(credentity)
    pickled_data = crypto.decrypt(cryptdata)
    sequence_obj = pickle.loads(pickled_data)


    def actions():
        backspace = '\b'*(len(source_text)+1)                       # delete mnemonic chars
        keyboard.write(backspace, restore_state_after=False)
        keyboard.play(sequence_obj)
    callback = lambda: actions()
    return keyboard.add_word_listener(source_text, callback, match_suffix=match_suffix, timeout=timeout)

keyboard.add_abbreviation = __add_abbreviation

if __name__ == "__main__":
    if args.create:
        print "please input sequence:"
        record_sequence(args.create)     # create vault for credentity
        print "Done.."
        sys.exit(0)
    else:
        # TODO : add option to show installed vault.
        keyboard.add_abbreviation("nanigmail-","nani")              # note you can't use char that requires combined keys here, such as @
        keyboard.add_abbreviation("ever-","ever")
        keyboard.add_abbreviation("decen-","decen")
        keyboard.add_abbreviation("anpa-","z2X")
        print "begin to intercept!!!"
        keyboard.wait()

