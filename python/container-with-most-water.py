#container with most water
#difficulty: medium
#language: python
#link: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:

        res=0
        i=0
        j=len(height)-1
        while i<j:
            a=abs(i-j)
            b=(min(height[i],height[j]))
            new=a*b
            res=max(res,new)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res
