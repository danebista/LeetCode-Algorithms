class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0 or nums==None:
            return 1
        
        containsOne = 0
        for i in range(len(nums)):
            if nums[i]==1:
                containsOne = 1
                
            elif nums[i]<=0 or nums[i]> len(nums):
                nums[i]=1
            
        if containsOne==0:
            return 1
            
        for i in range(len(nums)):
            index= abs(nums[i])-1
            
            if nums[index]>0 :
                nums[index]= -1 * nums[index]
        
        for i  in range(len(nums)):
            if nums[i]>0:
                return i + 1
        
        return n+1
        