class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=nums[0]
        for i in range (1,len(nums)):
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])
        return True
        