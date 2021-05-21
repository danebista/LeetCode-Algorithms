class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1

            while(l<r):
                sums= nums[l]+nums[r]+ a
                
                if sums>0:
                    r-=1
                
                if sums<0:
                    l+=1
                
                if sums==0:
                    ans.append([a,nums[l],nums[r]])
                    ]+=1
                    r-=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
                    while(nums[r]==nums[r+1] and l<r):
                        r-=1

        return ans