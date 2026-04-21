#find-the-index-of-the-first-occurrence-in-a-string
#difficulty:easy
#language: python
#link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ind=None
        l=len(needle)
        for i in range(len(haystack)):
            if needle==haystack[i:i+l]:
                ind=i
                break
        if ind==None:
            ind=-1
        return ind
