#contains duplicate 2
#difficulty: easy
#language: python
#link:https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        d={}
        for i,n in enumerate(nums):
            if n in d :
                if abs(i - d.get(n)) <= k:
                    return True
            d.update({n:i})
        return False
