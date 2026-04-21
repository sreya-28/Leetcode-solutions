#remove duplicates from sorted array
#difficulty: easy
#language: python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val=nums[0]
        k=1
        for i in range (1,len(nums)):
            if nums[i]!=val:
                val=nums[k]=nums[i]
                k+=1
        return k
