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


def find_val(matrix, target):
    row, col = len(matrix), len(matrix[0])
    top = 0
    bot = row
    # find row
    while top <= bot:
        m = (top+bot)//2
        if matrix[m][-1] < target:
            top = m+1
        elif matrix[m][0] > target:
            bot = m-1
        else:
            break
    # find target
    if not top <= bot:
        return False
    print(matrix[m])
    l = 0
    r = col - 1
    while l < r:
        md = (r+l)//2
        if matrix[m][md] < target:
            l = md + 1
        elif matrix[m][md] > target:
            r = md - 1
        else:
            print(matrix[m][md])
            return True
    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(find_val(matrix, target))
