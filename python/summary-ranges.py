#summary ranges
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        l = []
        start = nums[0]

        for i in range(1, len(nums)):
           
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    l.append(str(start))
                else:
                    l.append(str(start) + "->" + str(end))
                start = nums[i]  
        end = nums[-1]
        if start == end:
            l.append(str(start))
        else:
            l.append(str(start) + "->" + str(end))

        return l
