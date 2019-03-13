"""
Encrypt or decrypt the contents of a message file using a random key.
"""

import cipher_functions

KEY_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message1.txt'
MODE = 'e'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the key from a file called KEY_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt.
    """
    inp1 = open(KEY_FILENAME, 'rt')
    inp2 = open(MSG_FILENAME, 'rt')
    # read the key and the text into a variable
    KEY = cipher_functions.read_deck(inp1)
    TEXT = cipher_functions.read_messages(inp2)
    # output the string of encrpted or decrypted message
    print (cipher_functions.process_messages(KEY, TEXT, MODE))
    pass
# run the main function

if(__name__ == "__main__"):
    main()
