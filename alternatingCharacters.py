'''You are given a string containing characters A and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
For example, given the string, s=AABAAB remove an A at positions 0 and 3 to make ABAB in 2 deletions.'''

def alternatingCharacters(string):
    ''' function to remove duplicate characters next to each other and return the total number of deletion'''
    deletion = 0
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            deletion += 1
    print(deletion)

alternatingCharacters('AABBAACBBCCB') #5
alternatingCharacters('AAAA') #3
alternatingCharacters('BBBBB') #4
alternatingCharacters('ABABABAB') #0
alternatingCharacters('BABABA') #0
alternatingCharacters('AAABBB') #4