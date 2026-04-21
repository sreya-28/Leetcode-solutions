#reverse words in a string
#difficulty: medium
#language: python
#link:https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        n=s.split()[::-1]
        j=" ".join(n)
        return j
