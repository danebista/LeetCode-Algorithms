class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        
        def recursiveCombo(index, t, nL):
            if (t == 0):
                ans.append(list(nL))
                return
            
            for i in range(index, len(candidates)):
                if i>index and candidates[i]==candidates[i-1]: 
                    continue
                
                if (candidates[i]> t):
                    break
                
                nL.append(candidates[i])
                recursiveCombo(i+1, t-candidates[i], nL)
                nL.pop()
            
        
        candidates.sort()
        recursiveCombo(0,target, [])
        return ans