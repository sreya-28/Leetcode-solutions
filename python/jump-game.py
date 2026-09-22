#jump game
#difficulty: medium
#language: python
#link: https://leetcode.com/problems/jump-game/description
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i in range(len(nums)):
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])
        return True
