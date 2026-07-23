class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(temp,st):
            res.append(temp[:])
            for i in range (st,len(nums)):
                if i>st and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                backtrack(temp,i+1)
                temp.pop()
        backtrack([],0)
        return res        
        