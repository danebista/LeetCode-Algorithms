class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        for stra in strs:
            word="".join(sorted(stra))
            
            if word not in dict:
                dict[word]=[stra]
            else:
                dict[word].append(stra)
        result=[]
        
        for allValues in dict.values():
            result.append(allValues)
            
        return result
        