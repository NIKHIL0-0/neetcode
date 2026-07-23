class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(temp,st,tot):
            if tot==target:
                res.append(temp[:])
                return
            if tot>target:
                return
            for i in range (st,len(nums)):
                temp.append(nums[i])
                backtrack(temp,i,tot+nums[i])
                temp.pop() 
        backtrack([],0,0)
        return res



        