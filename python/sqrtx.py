#sqrt(x)
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        import math as m
        return floor(m.sqrt(x))
