class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        res=0
        for i in nums:
            if i-1 in nums:
                continue
            maxi=1
            while i+maxi in nums:
                maxi+=1
            res=max(maxi,res)
        return res
            

        