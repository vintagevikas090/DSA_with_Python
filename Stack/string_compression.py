'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

'''
from typing import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        s = []
        new_str = ''
        for i in chars:
            if len(s) == 0:
                s.append(i)
            elif s[-1] == i:
                s.append(i)
            else:
                c = s.pop()
                cnt = 1
                if len(s) != 0:
                    while s[-1] == c:
                        cnt+=1
                        s.pop()
                        if len(s) == 0:
                            break
                    new_str += c
                    new_str += str(cnt)
                else:
                    new_str += c

                s.append(i)
        
        if len(s) == 1:
            new_str += s[0]
        else:
            cnt = 0
            p = ''
            while len(s) != 0:
                p = s.pop()
                cnt += 1
            new_str += p
            new_str += str(cnt)


        chars.clear()
        for i in new_str:
            chars.append(i)
        return len(chars)