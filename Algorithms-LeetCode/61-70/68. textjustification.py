class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return
        
        result = []
        curr = []
        num_of_letters = 0
        
        for w in words:
            if len(w) + num_of_letters + len(curr)> maxWidth:
                if len(curr) == 1:
                    result.append(curr[0] + ' '* (maxWidth - num_of_letters))
                
                else:
                    num_of_spaces = maxWidth - num_of_letters
                    space, extra = divmod(num_of_spaces, len(curr)-1)
                    
                    for i in range(extra):
                        curr[i] +=' '
                    
                    result.append((' '*space).join(curr))
                curr=[]
                num_of_letters=0
            
            curr.append(w)
            num_of_letters += len(w)
        
        result.append(' '.join(curr)+ ' ' * (maxWidth-num_of_letters-len(curr)+1))
                
        return result
        