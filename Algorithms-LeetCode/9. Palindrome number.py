class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or abs(x)>2**31-1:
            return False
        
        rev=0
        s=x
        r=0
        while (x):
            r=x % 10
            x=x//10
            rev=rev*10+r
        
        if rev==s: return True
        
        return False
        