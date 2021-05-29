class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return None
        
        l,r=0,0
        
        while l < len(nums):
            if nums[l]!=val:
                print(l)
                nums[r]=nums[l]
                r+=1
            
            l+=1
        return r
        