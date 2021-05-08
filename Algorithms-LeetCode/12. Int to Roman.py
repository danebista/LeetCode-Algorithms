class Solution:
    def intToRoman(self, num: int) -> str:
        
        numberListKeys=[1, 4,5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        numberList=['I', 'IV','V', 'IX', 'X', 'XL', 'L', 'XC','C', 'CD', 'D', 'CM','M']
        answer=''
        numLen= len(numberList)-1
        
        while(num>0):
         
            if numberListKeys[numLen]<=num:
                answer+=numberList[numLen]
                num=num-numberListKeys[numLen]
            
            else:
                numLen-=1
        
                
        return answer        
        