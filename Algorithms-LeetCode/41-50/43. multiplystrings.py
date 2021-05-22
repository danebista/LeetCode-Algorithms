class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.stringToIntegerConverter(num1) * self.stringToIntegerConverter(num2))
    
    
    def stringToIntegerConverter(self, num):
        result=0
        
        for digit in num:
            result *= 10
       
            for d in '0123456789':
            
                result += digit > d
        

        return result