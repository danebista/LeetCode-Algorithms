class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest=100000000000
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
                
            l=i+1
            r=len(nums)-1
            
            while l<r:
                sumNos=a+nums[l]+nums[r]
    
                if sumNos==target:
                    return sumNos
                elif sumNos>target:
                    r-=1
                 
                    if abs(target-sumNos)<abs(target-closest):
                        closest=sumNos
                    while(nums[r]==nums[r+1] and l<r):
                        r-=1
                    
                else:
                  
                    l+=1
                    if abs(sumNos-target)<abs(target-closest):
                        closest=sumNos
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
        
        return closest  