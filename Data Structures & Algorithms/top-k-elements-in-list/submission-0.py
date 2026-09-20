class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        dic=Counter(nums)
        ls=list(dic.items())
        ls.sort(key= lambda x:x[1],reverse=True)
        res=[key for key,val in ls[:k]]
        return res


        