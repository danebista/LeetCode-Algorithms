class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        resL=0
        if len(s)== 0:
            return None
        
        for i in range(len(s)):
            l=i
            r=i
            
            while l>=0 and r< len(s) and s[l]==s[r]:
                if r-l+1> resL:
                    resL=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
         
         
        for i in range(len(s)):
            l=i
            r=i+1
            
            while l>=0 and r< len(s) and s[l]==s[r]:
                if r-l+1> resL:
                    resL=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res
         