#two sum
#difficulty: easy
#language: python
#link: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
