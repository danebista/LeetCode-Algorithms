class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        
        if n<=2: return 0
        
        maxLeft = height[0]
        maxRight= height[n-1]
        l=1
        r=n-2
        t=0
        while(l<=r):
            if maxLeft<maxRight:
                if maxLeft <= height[l]:
                    maxLeft = height[l]
                
                else:
                    t +=  (maxLeft-height[l])
                l+=1
            
            else:
                if maxRight<=height[r]:
                    maxRight= height[r]
                    
                else:
                    t+=(maxRight-height[r])
                r-=1
        
        return t
        