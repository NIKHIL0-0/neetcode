class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    return True
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False
        for i in range(len(matrix)):
            if matrix[i][0]<=target<=matrix[i][-1]:
                return search(matrix[i])
        return False
        
        

        