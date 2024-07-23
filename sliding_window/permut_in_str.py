'''
problem statement:  Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''


def check_inclusion(s1, s2):
    # Idea: Slide and check count_dict
    s1_dict = {}
    for v in s1:
        s1_dict[v] = s1_dict.get(v, 0) + 1

    l = 0
    r = len(s1)

    def count_letter(min_str):
        count = {}
        for v in min_str:
            count[v] = count.get(v, 0) + 1
        return count == s1_dict

    for i in range(len(s2)):
        if count_letter(s2[i:i+r]):
            return True
    return False


s1 = "ab"
s2 = "eidbaooo"
s1 = "ab"
s2 = "eidboaoo"
s1 = "a"
s2 = "ab"
s1 = "adc"
s2 = "dcda"
print(check_inclusion(s1, s2))
