'''
Problem Statement: Given a string s, find the length of the longest
substring
 without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


def longest_substring(s):
    l = 0
    r = 0
    char_set = set()
    res = 0
    while r < len(s):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r-l+1)
        print(l, r, char_set, res)
        r += 1

    return res


s = "abcabcbb"
s = "pwwkew"
#s = "bbbb"

print(longest_substring(s))
