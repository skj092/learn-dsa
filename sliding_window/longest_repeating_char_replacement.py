'''
Problem Statement: You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''


def char_replacement(s, k):
    count_dict = {}

    l = 0
    res = 0
    for r in range(len(s)):
        count_dict[s[r]] = count_dict.get(s[r], 0) + 1

        if (r-l+1) - max(count_dict.values()) > k:
            count_dict[s[l]] -= 1
            l += 1

        res = max(res, r-l+1)

    return res


s = "AABABBA"; k = 1
s = "ABAB"; k = 2
#s = "ABAA"; k = 0
print(char_replacement(s, k))
