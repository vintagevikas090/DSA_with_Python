'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

class Solution:
    def uniqueOccurrences(self, arr) -> bool:

        # Method 1
        '''freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        
        freq_arr = []
        for f in freq.values():
            freq_arr.append(f)

        for i in freq_arr:
            if freq_arr.count(i) > 1:
                return False

        return True'''


        # Method 2
        '''freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        
        freq_arr = []
        for f in freq.values():
            if f not in freq_arr:
                freq_arr.append(f)
            else:
                return False

        return True'''

        # Method 3
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        s = set()
        for f in freq.values():
            s.add(f)

        return len(freq) == len(s)






