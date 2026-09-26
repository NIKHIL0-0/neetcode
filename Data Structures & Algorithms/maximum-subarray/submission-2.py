class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        temp=nums[0]
        for i in (nums[1:]):
            temp = max(i, temp + i)
            ans=max(ans,temp)
        return ans