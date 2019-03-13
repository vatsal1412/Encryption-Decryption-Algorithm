# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def convert(letter):
    '''
    (str or int) -> int or str
    this function takes in a single upper case character and return its int
    value A = 0, B = 1 ... Z = 25 or if an int value is passed then it will
    return a letter corresponding to that int
    REQ: letter to be a single upper case character or letter <= 25
    >>> convert("A")
    0
    >>> convert("Z")
    25
    >>> convert(0)
    A
    >>> convert(25)
    Z
    '''
    # assign alpha to a list of character
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z']
    convert = ''
    # check whether a int is passed in or a string
    if (type(letter) == str):
        convert = alpha.index(letter)
    elif (type(letter) == int):
        convert = alpha[letter]
    # find letter in the list and return its index value
    return convert


def clean_message(inp_message):
    '''
    (str) -> str
    This function takes in an input message and cleans it up to include only
    capatilized alphabets and returns it
    REQ: one line of non-empty string
    >>>clean_message("This is a sample Input Message")
    THISISASAMPLEINPUTMESSAGE
    >>>clean_message("this-is-a-sample-input-message")
    THISISASAMPLEINPUTMESSAGE
    '''
    out_message = ''
    # loops through the message removing any characters that are not alphabets
    # storing the result in out_message
    for i in inp_message:
        if (i.isalpha() == True):
            out_message += i
    return(out_message.upper())


def encrypt_letter(char, key):
    '''
    (str, int) -> str
    This function takes in a character and a keystream value and encrypts it
    by adding the value togather mod 26
    REQ: char to be a string
    REQ key <= 26
    >>> encrypt_letter('A',8)
    'I'
    >>> encrypt_letter('Y',14)
    'M'
    '''
    encrypt_int = 0
    # convert char to int and add with key
    encrypt_int = (convert(char) + key) % 26
    # return the encrypted letter
    return convert(encrypt_int)


def decrypt_letter(char, key):
    '''
    (str, int) -> str
    This function takes in a character and a keystream value and decrypts it
    by subtracting the value mod 26
    REQ: char to be a string
    REQ key <= 26
    >>> decrypt_letter('I',8)
    'A'
    >>> decrypt_letter('M',14)
    'Y'
    '''
    decrypt_int = 0
    # convert char to int and subtract from key
    decrypt_int = (convert(char) - key) % 26
    # return the decrypted letter
    return convert(decrypt_int)


def swap_cards(deck, ind):
    '''
    (list of int, int) -> NoneType
    This function take in a list of int representing a deck of cards and an
    index value, it then take the int at the index value and swap it with the
    card the follows it
    REQ: list of int with more then 1 elements
    REQ: index value to be in range of the numbers of elements in the deck
    '''
    # set i to the index of the card you wish to switch
    i = ind
    # if the card you wish to swap is the last card in the deck then swap it
    # with the first card in the deck
    if (ind == len(deck) - 1):
        j = 0
    else:
        j = i + 1
    # perform the swap
    deck[i], deck[j] = deck[j], deck[i]


def move_joker_1(deck):
    '''
    (list of int) -> NoneType
    STEP : 1
    This function takes in a list of int representing a deck of cards, it then
    finds the first joker and swaps it with the card that follows it
    REQ: deck should have two Jokers
    '''
    # call the swap_card function on JOKER1
    swap_cards(deck, deck.index(JOKER1))


def move_joker_2(deck):
    '''
    (list of int) -> NoneType
    STEP : 2
    This function takes in a list of int representing a deck of cards, it then
    finds the second joker and swaps it twice with the card that follows it
    REQ: deck should have two Jokers
    '''
    # call the swap_card function twice on JOKER2
    swap_cards(deck, deck.index(JOKER2))
    swap_cards(deck, deck.index(JOKER2))


def triple_cut(deck):
    '''
    (list of int) -> NoneType
    STEP : 3
    This function perform a triple cut meaning that all the cards before the
    first joker goes at the bottom of the deck and all the cards after
    the second joker move to the top of the deck
    REQ: deck should have two Jokers
    '''
    # seperate the deck into 3 diffrent parts, top, middle and bottom
    top = deck[:min(deck.index(JOKER1), deck.index(JOKER2))]
    bottom = deck[max(deck.index(JOKER1), deck.index(JOKER2))+1:]
    middle = deck[min(deck.index(JOKER1), deck.index(JOKER2)):
                  max(deck.index(JOKER1), deck.index(JOKER2))+1]
    # mutate list to put the bottom part at the top and top at the bottom
    deck[:] = bottom + middle + top


def insert_top_to_bottom(deck):
    '''
    (list of int) -> NoneType
    STEP : 4
    This function takes the bottom card and read its value v, it then take the
    v number of cards and puts them just above the bottom most card
    REQ: deck should have two Jokers
    '''
    # if the bottom card is JOKER2 than take the value of JOKER1
    if (deck[len(deck) - 1] == JOKER2):
        v = JOKER1
    else:
        v = deck[len(deck) - 1]
    # seperate the deck into the top, rest and bottom
    top = deck[:v]
    rest = deck[v:len(deck)-1]
    bottom = deck[len(deck)-1:]
    # concatnate the three parts to mutate the old deck
    deck[:] = rest + top + bottom


def get_card_at_top_index(deck):
    '''
    (list of int) -> int
    STEP : 5
    This function takes the value of the top card as an index and return the
    value of that card if its a second JOKER2 then take the value of JOKER1
    REQ: deck should have two Jokers
    '''
    # if the top card is JOKER2 than take the value of JOKER1
    if (deck[0] == JOKER2):
        v = JOKER1
    else:
        v = deck[0]
    # return the card value at index v
    return deck[v]


def get_next_value(deck):
    '''
    (list of int) -> int
    This function runs the the five function to get the next potential
    keystream value
    REQ: deck should have two Jokers
    '''
    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    return get_card_at_top_index(deck)


def get_next_keystream_value(deck):
    '''
    (list of int) -> int
    This function runs the the five function to get the next potential
    keystream value until its within the range on 1-26
    REQ: deck should have two Jokers
    '''
    # set the key to joker1 by default to run the loop atleast once
    key = JOKER1
    # loop until you get a key stream outher that the jokers
    while (key == JOKER1 or key == JOKER2):
        key = get_next_value(deck)
    # return the key value
    return key


def process_message(deck, text, mode):
    '''
    (list of int, str, str) -> str
    This function takes a deck of card, some text and the mode(enrypt or
    decrypt, it then runsthe text trough the specified mode returning the
    processed text
    REQ: deck to have the number 27 and 28 (i.e. jokers)
    REQ: text to be a non empty string
    REQ: 'e' or 'd' for encrypt or decrypt
    '''
    # set default values for key, out_text and in_text
    key = []
    in_text = clean_message(text)
    out_text = ''
    # loop through the length of in_text and get the key to encrypt the message
    # with
    for i in in_text:
        key.append(get_next_keystream_value(deck))
    for j in range(len(key)):
        if (mode == 'e'):
            out_text += encrypt_letter(in_text[j], key[j])
        elif (mode == 'd'):
            out_text += decrypt_letter(in_text[j], key[j])
    return out_text


def process_messages(deck, text, mode):
    '''
    (list of int, list of str, str) -> list of str
    This function takes a deck of card, some list of text and the mode(enrypt
    or decrypt, it then runs the text trough the specified mode returning the
    processed list of text
    REQ: deck to have the number 27 and 28 (i.e. jokers)
    REQ: text to be a non empty list of strings only
    REQ: 'e' or 'd' for encrypt or decrypt
    '''
    # creat a default output list
    out_list = []
    # loop through each string in the list ane create a list of processed
    # string
    for i in text:
        out_list.append(process_message(deck, i, mode))
    return out_list


def read_messages(inp):
    '''
    (file open for reading) -> list of str
    this function reads a file into a list of strings seperated at newline
    character
    REQ: file to contain atleast one string character
    '''
    # read the file into one string
    inp_text = inp.read()
    # split the string at every newline character and return it
    out_text = inp_text.split("\n")
    return out_text


def read_deck(inp):
    '''
    (file open for reading) -> list of int
    this function reads a file of int into a list of int seperated at newline
    and space character
    REQ: file to contain jokers
    '''
    # read the string of numbers into inp_int
    inp_int = inp.read()
    # create an empty list
    out_text = []
    # loop thourgh the list of string and cast it to list of int
    for i in inp_int.split():
        out_text.append(int(i))
    # return the list
    return out_text
