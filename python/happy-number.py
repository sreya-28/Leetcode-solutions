#happy number
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/happy-number/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        l=[]
        while n not in l:
            l.append(n)
            while n>0:
                r=n%10
                sum=sum+(r*r)
                n=n//10
            n=sum
            sum=0
        if 1 in l:
            return True
        else:
            return False
