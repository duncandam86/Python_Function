from collections import Counter

def pickNumbers(arr):
    d = Counter(arr)
    print(d)
    ans = 0
    '''Given an array of integers, find and print the maximum number of integers 
    you can select from the array such that the absolute 
    difference between any two of the chosen integers is less than or equal to 1. 
    For example, if your array is a = [1, 1, 2, 2, 4, 4, 5, 5, 5], 
    you can create two subarrays meeting the criterion:  [1 ,1 ,2 ,2] and [4, 4, 5, 5, 5]. 
    The maximum length subarray has 5 elements.'''
    for i in d.keys():
        ans = max(int(d[i]) + int(d[i+1]), ans)
    print(ans)

a = [1, 1, 2, 2, 4, 4, 3, 3, 1,0,0,0,0,0,0,0,0,0]
pickNumbers(a) 