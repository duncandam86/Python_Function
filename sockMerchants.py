'''John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
For example, there are n =7 socks with colors ar = [1,2,1,2,1,3,2] . 
There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. The number of pairs is 2.'''
from collections import Counter
def sockMerchant(n, arr):
    '''n: the number of socks in the pile, ar: the colors of each sock'''
    d = Counter(arr)
    count = 0
    print(d)
    for i in d.keys():
        count += d[i]//2
    print(count)

ar = [3,2,1,2,1,3,2,3,4,4,2,5,6]
n = len(ar)
sockMerchant(n, ar)

ar1 = [10,20,20,10,10,30,50,10,20]
n = len(ar1)
sockMerchant(n, ar1)