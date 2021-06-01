class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="" or len(s)==0: return 0
        l=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' 'and l!=0: 
                break
            if s[i] != ' ':
                l+=1
        
        return l