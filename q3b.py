from q3a import *

def decode_ciphertext():

    ## map a character to a number
    char_map = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
        'i' : 8,
        'j' : 9,
        'k' : 10,
        'l' : 11,
        'm' : 12,
        'n' : 13,
        'o' : 14,
        'p' : 15,
        'q' : 16,
        'r' : 17,
        's' : 18,
        't' : 19,
        'u' : 20,
        'v' : 21,
        'w' : 22,
        'x' : 23,
        'y' : 24,
        'z' : 25,
    }

    ## map a number to a character
    num_to_char_map = {
        0 : 'a',
        1 : 'b',
        2 : 'c',
        3 : 'd',
        4 : 'e',
        5 : 'f',
        6 : 'g',
        7 : 'h',
        8 : 'i',
        9 : 'j',
        10 : 'k',
        11 : 'l',
        12 : 'm',
        13 : 'n',
        14 : 'o',
        15 : 'p',
        16 : 'q',
        17 : 'r',
        18 : 's',
        19 : 't',
        20 : 'u',
        21 : 'v',
        22 : 'w',
        23 : 'x',
        24 : 'y',
        25 : 'z'
    }

    ## open and load the ciphertext
    ciphertext = ''
    with open('./ciphertext.txt') as f:
        ciphertext = f.readlines()[0]

    ## get the secret key
    secret_key_string = find_secret_key()

    ## map the secret key to a number representation
    secret_key_number_lst = [ num_to_char_map[i] for i in secret_key_string ]

    plain_text = ''

    # for every n chars, where n is secret_key length
    while ciphertext:

        ## grab n chars from ciphertext
        section = ciphertext[0: len(secret_key_string)]

        ## for every char in the section
        for i, char in enumerate(section):

            ## map the char and ith position to a number


