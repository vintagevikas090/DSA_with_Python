'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''

class Solution:
    def decodeString(self, st: str) -> str:
        if len(st) < 2:
            return st
        s = []
        digit = '0123456789'
        for i in st:
            ns = ''
            if i == ']':
                if len(s) != 0:
                    temp = ''
                    while s[-1] != '[':
                        temp += s.pop()
                s.pop()
                n = ''
                while len(s) != 0 and s[-1] in digit:
                    n += s.pop()
                n = n[::-1]
                for i in range(int(n)):
                    ns += temp
                s.append(ns)
            else:
                s.append(i)
        output = ''
        for i in s:
            output += i[::-1]
        return output