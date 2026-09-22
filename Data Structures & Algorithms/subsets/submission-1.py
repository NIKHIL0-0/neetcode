class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(cur,temp):
            res.append(temp[:])
            for i in range (cur,len(nums)):
                temp.append(nums[i])
                backtrack(i+1,temp)
                temp.pop()
        backtrack(0,[])
        return res

        