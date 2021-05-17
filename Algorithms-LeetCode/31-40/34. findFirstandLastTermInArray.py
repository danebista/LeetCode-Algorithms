class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binarySearch(nums, target, True), self.binarySearch(nums, target, False)]
    
    def binarySearch(self, nums, target, biasFlag):
        l,r = 0, len(nums) - 1
        i=-1
            
        while(l <= r):
            mid = (l+r) // 2
            
            if target > nums[mid]:
                l=mid+1
            
            elif target<nums[mid]:
                r = mid - 1
            
            else:
                i=mid
                if (biasFlag):
                    r=mid-1
                else:
                    l=mid+1
        
        return i
        