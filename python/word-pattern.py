#word pattern
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sp={}
        ps={}
        s1=s.split(" ")
        p=list(pattern)
        if len(s1)!=len(p):
            return False
        for i in range(len(p)):
            c1=s1[i]
            c2=p[i]
            if c1 in sp and sp[c1]!=c2:
                return False
            if c2 in ps and ps[c2]!=c1:
                return False
            sp[c1]=c2
            ps[c2]=c1
        return True
         
