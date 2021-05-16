''' 
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         median1, median2 = -1,-1
        m, n =  len(nums1), len(nums2)
        maxlength = m + n
        l,r=0,0
        for i in range(maxlength//2 + 1):
            median2=median1
            if (l<m and r<n):
                if nums1[l]<=nums2[r]:
                    median1= nums1[l]
                    l+=1
                else:
                    median1 = nums2[r]
                    r+=1
            elif (l<m):
                median1=nums1[l]
                l+=1
            else:
                median1=nums2[r]
                r+=1
            
        if (m+n) % 2 ==1 :
            return median1
        else:
            return (median1+median2)/2
        