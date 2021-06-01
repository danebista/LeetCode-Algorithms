class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumpsMade = 1
        
        if n == 1 or nums[0] == 0:
        
            return 0
        
        farthest = nums[0]
        current_end = nums[0]
        
        for i in range(1, n):
           
            if i == n-1:
                return jumpsMade

            farthest =max(farthest, i + nums[i])
            
            if i == current_end:
                jumpsMade += 1
                current_end = farthest
        
        return jumpsMade

