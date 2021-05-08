class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue
            
            l,r=i+1,len(nums)-1
            while(l<r):
                threeSums=a +nums[l]+nums[r]
                if threeSums>0:
                    r-=1
                elif threeSums<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                        
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
        return ans