class Solution:
    def countAndSay(self, n: int) -> str:
        res=''
        if n==1:
            return "1"
        
        previousValue = self.countAndSay(n-1)
        count = 1
        len_nums = len(previousValue)
        
        for i in range(len_nums):
            if i == len_nums - 1 or (i+1 < len_nums and previousValue[i] != previousValue[i+1]):
                res += str(count) + previousValue[i]
                count = 1
            else:
                count += 1
        return res
            