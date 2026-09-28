class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        good=set()
        for i,j,k in triplets:
            if i>x or j>y or k>z:
                continue
            for idx,val in enumerate([i,j,k]):
                if val==target[idx]:
                    good.add(idx)
        return len(good)==3