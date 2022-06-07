
''' 
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
'''

def max_profit(prices):
    if prices == []:
        return 0

    total = 0
    index = 1 

    while index < len(prices):
        if prices[index - 1] < prices[index]:
            subtotal = prices[index] - prices[index - 1]
            total += subtotal 
        index += 1
    return total 


print(max_profit([7,1,5,3,6,4])) # 7
print(max_profit([1,2,3,4,5])) # 4
print(max_profit([7,6,4,3,1])) # 0