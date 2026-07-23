class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        ln=len(nums)
        def backtrack(temp,seen):
            if len(temp)==ln:
                res.append(temp[:])
                return
            for i in range (ln):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                temp.append(nums[i])
                backtrack(temp,seen)
                x=temp.pop()
                seen.discard(x)
        backtrack([],set())
        return res
            
