# Longest Substring Without Repeating Characters
#difficulty: medium
#language: python
#link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        n=0
        if s== "":
            return 0
        
        for i in s:
            if i not in l:
                l.append(i)
            else:
                n=max(n,len(l))
                while i in l:
                    l.pop(0)

                l.append(i)
                
        n=max(n,len(l))
        return max(n,len(l))
        
