class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r=0
        n=len(nums)
        if n<=1: return n
        
        l,r=1,1
        
        while(l<n):
            if nums[l]==nums[l-1]:
                l+=1
            else:
                nums[r]=nums[l]
                r+=1
                l+=1
        
        return r
        