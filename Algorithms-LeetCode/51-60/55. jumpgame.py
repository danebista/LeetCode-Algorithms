class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n == 1:
        
            return True
        
        if n>1 and nums[0]==0:
            return False
        
        farthest=0
        
        for i in range(n):
            if farthest==n-1:
                return True
            if i > farthest:
                return False
            farthest =max(farthest, i + nums[i])
    
        return True