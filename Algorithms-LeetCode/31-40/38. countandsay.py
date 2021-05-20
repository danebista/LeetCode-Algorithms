class Solution:
    def countAndSay(self, n: int) -> str:
        res=''
        if n==1:
            return "1"
        
        previousIterator = self.countAndSay(n-1)
        count=1
        num=len(previousIterator)
        for i in range(num):
            if i==num-1 or (i+1< num and previousIterator[i]!=previousIterator[i+1]):
                res+=str(count)+str(previousIterator[i])
                count=1
            else:
                count+=1
        
        return res
            