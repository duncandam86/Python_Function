'''Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?'''

def maxToys(prices, k):
    '''prices: an array of integers representing toy prices, k: an integer, Mark's budget'''
    sorted_prices = sorted(prices)
    total_spent = 0
    size = len(prices) 
    count = 0
    for i in range (size):
        if sorted_prices[i] <= (k - total_spent):
            total_spent += sorted_prices[i] 
            count += 1 
        else: 
            break  
    print(count)

a = [1,12,5,111,200,1000,10]
k = 50
maxToys(a,k)
