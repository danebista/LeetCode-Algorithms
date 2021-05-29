''' Reverse an integer within the integer flow limits'''

class Solution:
    def reverse(self, x: int) -> int:
        a=1
        delta=1
        if  abs(x)> (2**31)-1:
            return 0
        
        if x<0:
            delta=-1
            x*=delta
        reverse=0
        
        while(x):
            r=x % 10
            x=x//10
            reverse=reverse * 10 + r
        
        if abs(reverse* delta)>2**31-1: 
            return 0
        else:
            return reverse * delta
            