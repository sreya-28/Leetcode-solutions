#merge sorted array
#difficulty: easy
#language: python 
#link: https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(m,m+n):
            nums1[i]=nums2[j]   
            j+=1
        for i in range(0,m+n):
            for j in range(i+1,m+n):
                if nums1[i]>nums1[j]:
                    temp=nums1[j]
                    nums1[j]=nums1[i]
                    nums1[i]=temp


               
