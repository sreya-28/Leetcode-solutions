#palindrom number
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if s==s[::-1]:
            return True
        else: return False
