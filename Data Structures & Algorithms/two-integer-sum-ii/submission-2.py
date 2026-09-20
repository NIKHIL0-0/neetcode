class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        cur=nums[l]+nums[r]
        while cur!=target and l<r:
            if cur>target:
                r-=1
            else:
                l+=1
            cur=nums[l]+nums[r]
        return [l+1,r+1]


        