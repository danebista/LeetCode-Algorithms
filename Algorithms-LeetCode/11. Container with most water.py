Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxHeight =0
        while l<r:
            
            tempHeight=min(height[l],height[r])*(r-l)
            
            if (tempHeight >maxHeight):
                maxHeight=tempHeight
            
            if (height[l]<height[r]):
                l+=1
            else:
                r-=1
        return maxHeight
            