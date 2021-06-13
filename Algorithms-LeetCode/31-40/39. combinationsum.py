class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        
        def recurser(index, targets, newList):
            if index == len(candidates):
                if targets == 0:
                    result.append(newList.copy())
                return
            if targets == 0:
                result.append(newList.copy())
                return
                
            if candidates[index] <=targets:
                newList.append(candidates[index])
                recurser(index, targets-candidates[index], newList)
                newList.pop()
            recurser(index+1, targets, newList)
        
        recurser(0, target, [])
        return result