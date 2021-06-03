from q1a import *
import matplotlib.pyplot as plt

ciphertext = ''
with open('./ciphertext.txt') as f:
    ciphertext = f.readlines()[0]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

plt.plot( letters ,num_of_occurences(ciphertext) )
plt.show()