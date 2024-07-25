'''
Problem Statement: You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''


def search_matrix(matrix, target):
    row = len(matrix)
    cols = len(matrix[0])
    # step 1: find row
    top = 0
    bot = row - 1

    while top <= bot:
        mid = (bot + top) // 2
        if matrix[mid][-1] < target:
            top = mid + 1
        if matrix[mid][0] > target:
            bot = mid - 1
        else:
            break
    # Step 2: Find value
    l = 0
    r = cols - 1
    while l < r:
        m = (r + l)//2
        if matrix[mid][m] > target:
            r = m - 1
        elif matrix[mid][m] < target:
            l = m + 1
        elif matrix[mid][m] == target:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(search_matrix(matrix, target))
