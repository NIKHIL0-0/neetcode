from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(x) for x in nums]
        res = []

        def compare(a, b):
            if a + b > b + a:
                return True
            return False

        while nums:
            best = 0

            for i in range(1, len(nums)):
                if compare(nums[i], nums[best]):
                    best = i

            res.append(nums[best])
            nums.pop(best)

        ans = "".join(res)

        return "0" if ans[0] == "0" else ans