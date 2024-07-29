'''
Problem Statement: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''


def longest(nums):
    unique = set(nums)
    res = 0

    for n in unique:
        # check if starting of the sequence
        if n-1 not in unique:
            length = 0
            while (n+length) in unique:
                length += 1
            res = max(length, res)
    return res


nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

print(longest(nums))
