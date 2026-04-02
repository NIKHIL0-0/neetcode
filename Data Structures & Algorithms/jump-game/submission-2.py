class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # pos = 0
        # curr = nums[0]
        # if len(nums)==1:
        #     return True
        # while pos < len(nums):
        #     moved = False  # track progress

        #     for i in range(pos + 1, min(len(nums), pos + nums[pos] + 1)):
        #         if i == len(nums) - 1:
        #             return True
        #         if curr < i + nums[i]:
        #             pos = i
        #             curr = i + nums[i]
        #             moved = True

        #     if not moved:
        #         return False  # no progress → stuck

        # return False
        maxoo=nums[0]

        for i in range (len(nums)):
            if i>maxoo:
                return False
            maxoo=max(maxoo,i+nums[i])
        return True