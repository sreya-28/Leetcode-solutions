#majority element
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]=d.get(i)+1
            else:
                d[i]=1
        v=max(d,key=d.get)
        if d[v]>(len(nums)/2):
            return v
