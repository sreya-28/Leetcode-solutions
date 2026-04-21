#isomorphic strings
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st={}
        ts={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)) :
            c1=s[i]
            c2=t[i]
            if c1 in st and st[c1]!=c2:
                return False
            if c2 in ts and ts[c2]!=c1:
                return False
            
            st[c1]=c2
            ts[c2]=c1
        return True
