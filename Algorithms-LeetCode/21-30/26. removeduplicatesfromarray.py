class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n<=1: return n
        
        r=1
        
        for l in range(1,n):
            if nums[l] != nums[l-1]:
                nums[r]=nums[l]
                r+=1
        
        return r