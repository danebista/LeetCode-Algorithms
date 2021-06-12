class Solution:
    def simplifyPath(self, path: str) -> str:
        broken_characters = path.split('/')
        finishedList = []
        
        for broken_character in broken_characters:
            
            if broken_character == '' or broken_character == '.':
                continue
                
            elif broken_character == '..':
                if len(finishedList) == 0: continue
                
                finishedList.pop()
            
            else:
                finishedList.append(broken_character)
        
        return  "/" + ("/").join(finishedList)
