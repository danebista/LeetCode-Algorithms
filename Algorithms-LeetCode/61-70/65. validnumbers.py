class Solution:
    def isNumber(self, s: str) -> bool:
        
        digits, symbols, e, decimal = False, False, False, False
        
        for char in s:
            
            if char in '0123456789':
                digits = True
            
            elif char in '+-':
                if symbols or digits or decimal:
                    
                    return False
                else:
                    
                    symbols = True
            
            elif char in 'eE':
                
                if not digits or e:
                    return False
                else:
                    e = True
                    digits = False
                    symbols = False
                    decimal = False
            
            elif char == '.':
                
                if decimal or e:
                    return False
                else: 
                    decimal = True
            
            else: 
                return False
        
                
        return digits 
        