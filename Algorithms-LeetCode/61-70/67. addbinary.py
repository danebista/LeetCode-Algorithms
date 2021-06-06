class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        aLength = len(a)
        bLength = len(b)
        if aLength< bLength:
            a = '0' *(bLength - aLength) + a
        elif bLength < aLength:
            b = '0' * (aLength - bLength) + b
        
        for i in range(len(a)-1,-1,-1):
            value = int(a[i]) + int(b[i]) + carry
            res=  str(value % 2) + res
            carry = value // 2
        
        if carry:
            res = "1" + res
        
        return res