"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sets=set()
        l=0
        result=0
        
        for r in range(len(s)):
            while s[r] in sets:
                
                sets.remove(s[l])
                l=l+1
            
            sets.add(s[r])
            result= result if result>r-l+1 else r-l+1
        
        return result
        