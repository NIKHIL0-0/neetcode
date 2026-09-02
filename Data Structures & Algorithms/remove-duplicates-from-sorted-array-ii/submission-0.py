class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp=-111111
        freq=0
        c=0
        for inx,i in enumerate(nums):
            if temp!=i:
                temp=i
                freq=1
            elif temp==i:
                freq+=1
                if freq>2:
                    nums[inx]=float('inf')
                    c+=1
        l=0
        r=0
        for r,i in enumerate(nums):
            while nums[l]!=float('inf') and l<r:
                l+=1
            if i!=float("inf") and nums[l]==float('inf'):
                nums[l],nums[r]=nums[r],nums[l]
        return len(nums)-c
            




            
        