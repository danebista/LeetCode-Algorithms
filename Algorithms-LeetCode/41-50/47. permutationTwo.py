class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashMap = {n:0 for n in nums}
        perms = []
        final = []
        
        for i in nums:
            hashMap[i]+=1
        
        def permuter():
            if len(perms)==len(nums):
                final.append(perms.copy())
                return
            
            for i in hashMap:
                if hashMap[i]>0:
                    perms.append(i)
                    hashMap[i]-=1
                    
                    permuter()
                    hashMap[i]+=1
                    perms.pop()
        permuter()
        return final            