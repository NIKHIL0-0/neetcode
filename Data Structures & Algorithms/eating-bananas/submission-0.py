import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        best=min(piles)
        def time(sp):
            time=0
            for i in piles:
                time+=math.ceil(i/sp)
            if time<=h:
                return True
            else:
                return False
        while l<=r:
            mid=(l+r)//2
            if time(mid):
                best=mid
                r=mid-1
            else:
                l=mid+1
        return best


        