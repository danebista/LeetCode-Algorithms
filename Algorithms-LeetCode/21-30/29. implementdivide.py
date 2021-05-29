class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_VALUE = -2**31
        MAX_VALUE = 2**31-1
        if divisor > MAX_VALUE: return 0
        if dividend < MIN_VALUE: return 0
     
        
        if dividend == MIN_VALUE and divisor==-1:
            return MAX_VALUE
 
       
        a=abs(dividend)
        b=abs(divisor)
       
        res=0
        while (a-b >=0):
            x=0 
            while((a-(b<<1<<x))>=0):
                x+=1
            
            res+=1<<x
            a-=b<<x
            
        if divisor>=0 and dividend>=0:
            return res
        elif divisor<=0 and dividend<=0:
            return res
        else:
            return -1* res
            