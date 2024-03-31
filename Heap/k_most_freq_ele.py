'''
Problem statement
You are given an Integer array ‘ARR’ and an Integer ‘K’.



Your task is to find the ‘K’ most frequent elements in ‘ARR’. Return the elements in any order.



For Example:

You are given ‘ARR’ = {1, 2, 2, 3, 3} and ‘K’ = 2. 

The answer will {2, 3} as 2 and 3 are the elements occurring most times.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
5 2
1 2 2 3 3 
Sample Output 1:
2 3
Explanation of Sample Input 1:
The answer will {2, 3} as 2 and 3 are the elements occurring the most number of times.
Sample Input 2:
2 2
1 2 
Sample Output 2:
1 2
Constraints:
1 <= 'N' <= 10^5
1 <= 'K' <= Number of unique elements in ‘ARR’
1 <= 'ARR[i]' <= 10^6

Time Limit: 1 sec
'''

from typing import List
import heapq

class element:
    def __init__(self, val, f):
        self.val = val
        self.f = f

    def __lt__(self, other):
        return self.f > other.f

    def __eq__(self, other):
        return self.f == other.f

def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    heap = []
    for num, frequency in freq.items():
        ele = element(num, frequency)
        heapq.heappush(heap, ele)

    res = []
    for i in range(k):
        curr = heapq.heappop(heap)
        res.append(curr.val)

    return res

    
l = [1, 2, 2, 3, 3]
ans = KMostFrequent(5, 2, l)
print(*ans)