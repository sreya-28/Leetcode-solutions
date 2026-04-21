#is subsequence
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/is-subsequence/
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c=0
        flag=0
        n=-1
        for i in range(len(s)):
            flag=0
            for j in range(len(t)):
                if s[i]==t[j] and j>n:
                    c+=1
                    flag=1
                    n=j
                    break
            if flag==0:
                break
        if c==len(s):
            return True
        else:
            return False
