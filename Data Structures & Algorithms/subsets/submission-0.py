class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(temp,st):
            res.append(temp[:])
            for i in range (st,len(nums)):
                temp.append(nums[i])
                backtrack(temp,i+1)
                temp.pop()
        backtrack([],0)
        return res
            
        

        