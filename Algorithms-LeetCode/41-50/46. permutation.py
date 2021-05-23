class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finalOutput= []
        
        if (len(nums)==1):
            return [nums.copy()]
        
        for i in range(len(nums)):
            n=nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
                
            finalOutput.extend(perms)
            nums.append(n)
        
        return finalOutput
        