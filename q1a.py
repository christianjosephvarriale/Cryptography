
def num_of_occurences( txt ):
    
    ## map a character to an integer
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

    ## create an empty list init to all 0's of length 26
    char_arr = [0 for i in range(26)]

    ## iterate through the text, every time we see a char increment that position in the char_arr
    for char in txt:
        char_arr[char_map[char]] += 1

    return char_arr
