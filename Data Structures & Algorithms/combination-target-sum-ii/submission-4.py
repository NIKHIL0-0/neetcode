class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def rec(st,temp):
            if sum(temp)==target:
                res.append(temp[:])
                return
            elif sum(temp)>target:
                return
            for i in range(st,len(nums)):
                if i>st and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                rec(i+1,temp)
                temp.pop()
        rec(0,[])
        return res
