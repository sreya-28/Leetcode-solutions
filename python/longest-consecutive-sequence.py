#Longest Consecutive Sequence
#difficulty: medium
#language: python
#link: https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new=sorted(set(nums))
        if len(nums)>0:
            key=new[0]
            maxl=0
            c=1
            for i in range(1,len(new)):
                if new[i]==key+1:
                    c+=1
                else:
                    maxl=max(maxl,c)
                    c=1
                key=new[i]
            maxl=max(maxl,c)
            return maxl  
        else:
            return 0
