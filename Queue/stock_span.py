'''Amit has been working with an organization called 'Money Traders' 
for the past few years. The organization is into the money trading business.
His manager assigned him a task. For a given array/list of stock's prices for N days,
find the stock's span for each day.

The span of the stock's price today is defined as the maximum number of 
CONSECUTIVE days(starting from today and going backwards) for which the price of the stock was
less than today's price.

For example, if the price of a stock over a period of 7 days are [100, 80, 60, 70, 60, 75, 85], 
then the stock spans will be [1, 1, 1, 2, 1, 4, 6].'''

def stockSpan(price, n) :
    #Your code goes here
    if n==0:
        return price
    
    spanlist = []

    if n == 1:
        return [1]
    
    for i in range(n-1, -1, -1):
        spanCount = 1
        j = i-1
        while j>=0 and price[j]<price[i]:
                spanCount = spanCount+1
                j = j - 1 
        spanlist.append(spanCount)
    

    return spanlist[::-1]

li = [int(i) for i in input().split()]
n = len(li)
output = stockSpan(li, n)
print('Daywise span data is: ')
print(output)
