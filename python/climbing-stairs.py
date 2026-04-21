#climbing stairs
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        d=[1,1]     #size
        for i in range(2,n+1):
            d.append(d[i-1]+d[i-2])
        return d[n]
