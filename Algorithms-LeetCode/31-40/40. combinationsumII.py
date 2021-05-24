class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def recurser(index,targets, newList):
            if targets==0:
                ans.append(newList.copy())
            
            
            for i in range(index, len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                
                if candidates[i]>targets:
                    break
                    
                newList.append(candidates[i])
                
                recurser(i+1, targets-candidates[i], newList)
                
                newList.pop()
            
            
            
        candidates.sort()
        recurser(0, target, [])
        
        return ans