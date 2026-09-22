class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        def bt(start,temp):
            res.append(temp[:])
            for i in range (start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                bt(i+1,temp)
                temp.pop()
        bt(0,[])
        return res
        