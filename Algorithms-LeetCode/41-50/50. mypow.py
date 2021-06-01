class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache={}
      
        def powAf(xe,num):
            if (xe,num) in cache: 
                
                return cache[(xe, num)]
            
            if num==0:
                return 1
            
            elif num<0:
                cache[(xe, num)] = powAf(1/xe, -num)
                return cache[(xe,num)]
            
            elif num % 2 == 0:
                cache[(xe, num)]= powAf(xe, num/2) * powAf(xe, num/2)
                return cache[(xe,num)]
            else:
                cache[(xe, num)] = xe * powAf(xe, num-1)
                return cache[(xe,num)]
            
        return powAf(x,n)
        