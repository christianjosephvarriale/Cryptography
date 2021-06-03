from q1a import *
from q2a import *

def find_secret_key():

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


    ## first open ciphertext and generate chunks
    ciphertext = ''
    with open('./ciphertext.txt') as f:
        ciphertext = f.readlines()[0]

    chunks = output_chuncked_text(ciphertext, 6)
    secret_key_string = ''

    ## for each chunk
    for chunk in chunks:

        occurence_lst = num_of_occurences( chunk )

        ## find the index where e is located due to max frequency 
        e_index = occurence_lst.index(max(occurence_lst))

        ## determine shift based on difference between e_index and standard e_index i.e. 4
        ## note we must wrap around by adding 26 if our shift is negative
        shift = e_index - 4
        if shift < 0:
            shift += 26

        ## add to secret_key string
        secret_key_string += num_to_char_map[shift]

    print(secret_key_string)
    return secret_key_string