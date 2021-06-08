class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        
        def fibo(num):
            if num in cache: return cache[num]
            
            
            if num<=2:
                cache[num] = num
                return cache[num]
            
            else:
            
                cache[num] = fibo(num-1)+ fibo(num-2)
    
                return cache[num]
            
        return fibo(n)
        