class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def rec(st,temp):
            if sum(temp)==target:
                res.append(temp[:])
                return
            elif sum(temp)>target:
                return
            for i in range (st,len(nums)):
                temp.append(nums[i])
                rec(i,temp)
                temp.pop()
        rec(0,[])
        return res