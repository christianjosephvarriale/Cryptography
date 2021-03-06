from q2a import *
from q1a import *
import matplotlib.pyplot as plt

ciphertext = ''
with open('./ciphertext.txt') as f:
    ciphertext = f.readlines()[0]

## letters in the alphabet for frequency analysis
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

## plot frequency analysis for single chunk
plt.plot( letters , num_of_occurences(output_chuncked_text(ciphertext, 6)[0]) )
plt.show()