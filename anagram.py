'''Alice is taking a cryptography class and finding anagrams to be very useful. 
We consider two strings to be anagrams of each other 
if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Alice decides on an encryption scheme involving two large strings 
where encryption is dependent on the minimum number of character deletions 
required to make the two strings anagrams. Can you help her find this number?

Given two strings, a and b, that may or may not be of the same length, 
determine the minimum number of character deletions required to make a  and  b anagrams. 
Any characters can be deleted from either of the strings.'''

import string
import numpy as np
def anagram (a,b):
    '''function to determine number of letters that need to be removed to make a,b anagram'''
    total = 0
    alphabet = list(string.ascii_lowercase)
    array_a = []
    array_b = []
    for letter in alphabet:
        x = a.lower().count(letter)
        array_a.append(x)
        y = b.lower().count(letter)
        array_b.append(y)
    difference = abs(np.array(array_a) -  np.array(array_b)).sum()
    print(abs(np.array(array_a) -  np.array(array_b)))
    total += difference
    print(total)

a = 'CUNT'
b = 'CANT'
anagram(a,b)
