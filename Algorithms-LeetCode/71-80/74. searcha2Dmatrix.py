class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) * len(matrix[0])-1
        
        while low <= high:
            mid = (low + high)//2
            value = matrix[mid//len(matrix[0])][mid % len(matrix[0])]    
            if value == target:
                return True
            elif value< target:
                low = mid+1
            else:
                high = mid-1
        return False
        