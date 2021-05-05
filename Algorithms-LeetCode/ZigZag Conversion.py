'''

P   A   H   N
A P L S I I G
Y   I   R
 "PAHNAPLSIIGYIR"


'''



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        flag= -1
        row=0
        final=[[] for x in range(numRows)]
        
        if numRows==1:
            return s
        for i in s:
            final[row].append(i)
            if (row==0 or row==numRows-1):
                flag=flag*-1
            
            row+=flag
        
            
        for i in range(len(final)):
            final[i]=''.join(final[i])
        
        return ''.join(final)
            