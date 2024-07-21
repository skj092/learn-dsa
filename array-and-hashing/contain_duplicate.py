'''
Problem Statement : Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''


def containsDuplicate(nums):
    S = set()
    for n in nums:
        if n in S:
            return True
        else:
            S.add(n)
    return False


if __name__ == '__main__':
    # Test Case 1
    nums = [1, 2, 3, 1]
    assert containsDuplicate(nums) == True

    # Test Case 2
    nums = [1, 2, 3, 4]
    assert containsDuplicate(nums) == False

    # Test Case 3
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert containsDuplicate(nums) == True

