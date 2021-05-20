class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        
        def recurserCombo(index, targets, newList):
           
         
            if (index==len(candidates)):
                if (targets==0):
                    
                    ans.append(list(newList))
                return
            
            if targets==0:
                ans.append(list(newList))
                return
                
            if (candidates[index]<=targets):
                    newList.append(candidates[index])
                    recurserCombo(index, targets-candidates[index], newList)
                    newList.pop()
            
            recurserCombo(index+1, targets, newList)
            
        recurserCombo(0, target, [])
        
        return ans
                     