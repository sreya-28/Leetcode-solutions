#plus one
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=0
        for i in digits:
            n=n*10+i
        n+=1
        l=[]
        while n!=0:
            l.append(n%10)
            n=n//10
        return l[::-1]
