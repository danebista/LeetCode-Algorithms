class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxYet=totalYet=nums[0]
        
        for i in nums[1:]:
            totalYet=max(i, totalYet+i)
            
            maxYet=max(maxYet, totalYet)
        
        return maxYet