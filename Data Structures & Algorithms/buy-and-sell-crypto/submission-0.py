class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit=0
        buy=nums[0]
        for i in nums[1:]:
            iff=i-buy
            if iff>profit:
                profit=max(profit,iff)
            else:
                buy=min(buy,i)
        return profit
        