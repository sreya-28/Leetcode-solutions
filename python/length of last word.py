#length of last word
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=s.split()
        return len(a[-1])
