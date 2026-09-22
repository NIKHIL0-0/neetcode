class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        seen=[False]*n
        def rec(temp):
            if len(temp)==n:
                res.append(temp[:])
                return
            for i in range(0,n):
                if seen[i]:
                    continue
                seen[i]=True
                temp.append(nums[i])
                rec(temp)
                temp.pop()
                seen[i]=False
        rec([])
        return res

        