class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap=[]
        for i in stones:
            heapq.heappush(heap,-i)
        while len(heap)>1:
            s1=-heapq.heappop(heap)
            s2=-heapq.heappop(heap)
            if s1==s2:
                continue
            else:
                heapq.heappush(heap,-(s1-s2))
        return -heap[0] if len(heap)!=0 else 0

        