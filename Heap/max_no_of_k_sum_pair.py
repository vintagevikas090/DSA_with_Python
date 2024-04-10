'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and 
remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
'''
from typing import *

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        freq = {}
        pair = 0
        for i in nums:
            expect = k - i
            if freq.get(expect, 0) > 0:
                # since we want no of operations, the pair will get deleted one by one
                # so inc pair by '1' (not freq[expect])
                pair += 1
                freq[expect] -= 1
            else:
                freq[i] = freq.get(i, 0) + 1
        return pair


        