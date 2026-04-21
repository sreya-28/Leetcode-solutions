#roman to integer
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/roman-to-integer/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=["I","V","X","L","C","D","M"]
        n=len(s)-1
        sum=0
        for i in range(len(s)):
            if s[i]=="M":
                sum+=1000
            elif s[i]=="D":
                if i!=n:
                    if s[i+1]=="M":
                        sum-=500
                    else:
                        sum+=500
                else:
                    sum+=500
            elif s[i]=="C":
                if i!=n:
                    if s[i+1] in l[5:]:
                        sum-=100
                    else:
                        sum+=100
                else:
                    sum+=100
            elif s[i]=="L":
                if i!=n:
                    if s[i+1] in l[4:]:
                        sum-=50
                    else:
                        sum+=50
                else:
                    sum+=50
            elif s[i]=="X":
                if i!=n:
                    if s[i+1] in l[3:]:
                        sum-=10
                    else:
                        sum+=10
                else:
                    sum+=10
            
            elif s[i]=="V":
                if i!=n:
                    if s[i+1] in l[2:]:
                        sum-=5
                    else:
                        sum+=5
                else:
                    sum+=5
            elif s[i]=="I":
                if i!=n:
                    if s[i+1] in l[1:]:
                        sum-=1
                    else:
                        sum+=1
                else:
                    sum+=1
            else:
                return Invalid
        return sum
