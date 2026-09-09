#roman to integer
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        rn={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        val=0
        if n==1:
            val=rn[s]
            return val
            
        for i in range(n-1):
            if rn[s[i]]>=rn[s[i+1]]:
                val+=rn[s[i]]
            else:
                val-=rn[s[i]]
        val+=rn[s[-1]]
        return val
