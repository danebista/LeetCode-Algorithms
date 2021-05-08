class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp=""
        if len(strs)==0: return lcp
        
        minLen=len(strs[0])
        
        for i in range(1, len(strs)):
            
            if len(strs[i])<minLen:
                
                minLen=len(strs[i])
         
        for i in range(minLen):
            start=strs[0][i]
            
            for j in range(1, len(strs)):
                if start != strs[j][i]:
                    return lcp
            lcp+=start
        return lcp
        