class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return None
        
        r=0
        
        for l in range(len(nums)):
            if nums[l]!=val:
                nums[r]=nums[l]
                r+=1
        
        return r
        
        