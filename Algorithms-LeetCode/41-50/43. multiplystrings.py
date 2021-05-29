class Solution:
    def multiply(self, num1: str, num2: str) -> str:
       
        output=[]
        is_zero_leading = True
        a= [0] * (len(num1)+len(num2))
        output=''
        for i in range(len(num1)-1, -1,-1):
            for j in range(len(num2)-1,-1,-1):
                
                value=int(num1[i]) * int(num2[j])+ a[i+j+1]
                
                a[i+j] += value //10
                a[i+j+1] = value % 10
        for i in range(len(a)):
            if a[i] !=0:
                is_zero_leading = False
            
            if is_zero_leading == False:
                output+=str(a[i])
        if output=="": return "0"
        
        return output
        