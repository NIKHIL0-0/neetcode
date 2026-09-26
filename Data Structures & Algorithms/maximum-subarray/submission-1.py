class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=float('-inf')
        temp=float('-inf')
        for i in (nums):
            ans=max(ans,temp)
            if i>temp+i:
                temp=i
                ans=max(ans,temp)
            else:
                temp+=i
                ans=max(ans,temp)
        return ans