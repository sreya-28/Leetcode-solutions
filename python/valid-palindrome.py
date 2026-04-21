#valid palindrome
#difficulty:easy
#language: python
#link:https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s="".join(char for char in s if char.isalnum())
        t=s[::-1]
        if s==t:
            return True
        else:
            return False
