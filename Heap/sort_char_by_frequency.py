'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
'''

import heapq
class pair:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        heap = []
        for f in freq:
            element = pair(f, freq[f])
            heapq.heappush(heap, element)
        
        res = ""
        while len(heap) != 0:
            ele = heapq.heappop(heap)
            frequency = ele.freq
            character = ele.char
            for i in range(frequency):
                res += character

        return res