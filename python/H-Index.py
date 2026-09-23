#H-Index
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/h-index/description/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i=len(citations)
        while i>=0:
            c=0
            for j in citations:
                if j>=i:
                    c+=1
            if c>=i:
                return i
            i-=1
        
    
