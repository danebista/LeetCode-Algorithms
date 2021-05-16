class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0: return []
        if len(s)==0: return []
        
        wordDict={}
        for i in words:
            wordDict[i]=wordDict[i] +1 if i in wordDict.keys() else 1
        
        wordCount = len(words)
        eachWord = len(words[0])
        res=[]
        for i in range(len(s)-len(words)+1):
            foundWords = {}
            
            for j in range(wordCount):
                startIndex=i+j*eachWord
                val = s[startIndex: startIndex+ eachWord]
                if (not val in wordDict.keys()):
                    break
                
                foundWords[val]= foundWords[val]+1 if val in foundWords.keys() else 1
                
                if foundWords[val]> wordDict[val]:
                    break
                
                if (j+1 == wordCount):
                    res.append(i)
        return res
            