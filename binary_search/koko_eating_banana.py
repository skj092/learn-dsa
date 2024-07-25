'''
Problem Statement: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

'''


def min_eating_speed(piles, h):
    def can_eat(hour):
        print(hour, sum([-(val // -hour) for val in piles]))
        return sum([-(val // -hour) for val in piles]) <= h
    l = 1
    r = max(piles)
    res = max(piles)
    while l <= r:
        m = (r + l) // 2
        if can_eat(m):
            res = min(res, m)
            r = m - 1
        else:
            l = m + 1
    return res


piles = [3, 6, 7, 11]
h = 8
piles = [30, 11, 23, 4, 20]
h = 5
piles = [312884470]
h = 968709470
print(min_eating_speed(piles, h))
