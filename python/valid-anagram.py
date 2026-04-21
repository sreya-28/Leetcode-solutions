#valid anagram
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag=0
        s1=sorted(list(s))
        t1=sorted(list(t))
        
        if len(s)!=len(t):
            return False
        else:
            if s1==t1:
                return True
            else:
                return False
