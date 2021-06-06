class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
            
        for i  in range(len(digits)-1, -1 ,-1):
        
            if digits[i] < 10:
                break
            
            if i==0:
                digits.insert(0, digits[i]//10)
                digits[i+1] = digits[i+1]%10
                break
                
            digits[i-1] += digits[i] // 10
            digits[i] = digits[i] % 10
            
        return (digits)
            