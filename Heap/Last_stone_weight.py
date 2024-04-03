'''
Problem statement
We have a collection of 'N' stones, each stone has a positive integer weight.

On each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights 'x' and 'y' with 'x' <= 'y'.
 The result of this smash will be:

1. If 'x' == 'y', both stones are totally destroyed;

2. If 'x' != 'y', the stone of weight 'x' is totally destroyed, and the stone of weight 'y' has a new weight equal to 'y - x'.
In the end, there is at most 1 stone left. Return the weight of this stone or 0 if there are no stones left.

Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= N <= 10^5
1 <= W <= 10^6

Time Limit: 1 sec
Sample Input 1:
1
10
Sample Output 1:
10
Explanation For Sample Input 1:
There is Only one stone so the weight of the last stone is 10
Sample Input 2:
3
1 9 5
Sample Output 2:
3 
'''

from sys import stdin
import sys
import heapq
sys.setrecursionlimit(10**7) 


def weightOfLastStone(stones, n) :
    # for max heap, multiply each value with -1
    stones = [-i for i in stones]

    heapq.heapify(stones) # now stones is a max_heap(with all weight --->as (-weight))

    while len(stones) > 1:
        x = -heapq.heappop(stones)
        y = -heapq.heappop(stones)

        if x != y:
            heapq.heappush(stones, y - x)

    if len(stones) == 0:
        return 0
    else:
        return -(stones[0])
    
#taking input using fast I/O
def takeInput() :
    n=int(input('No of stones: '))
    print('Enter the weight of the stones: ')
    stones=list(map(int, input().strip().split(" ")))

    return stones, n

#main
stones, n  = takeInput()
print(weightOfLastStone(stones, n))
