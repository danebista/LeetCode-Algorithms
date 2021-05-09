class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        
        if len(nums)<4 or not nums: return res
        nums.sort()
        
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]: continue
                sums=nums[i]+nums[j]
                l=j+1
                r=len(nums)-1
                    
                while (l<r):
                    sumNos=sums+nums[l]+nums[r]
                        
                    if sumNos < target:
                        l+=1
                    elif sumNos> target:
                        r-=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                
                        
        return res    
        