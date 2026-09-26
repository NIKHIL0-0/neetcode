class Solution:
    def jump(self, nums: List[int]) -> int:
        # from collections import deque

        # q = deque()
        # q.append((0, 0))
        # visited = {0}

        # while q:
        #     curr, step = q.popleft()

        #     if curr >= len(nums) - 1:
        #         return step

        #     for i in range(1, nums[curr] + 1):
        #         nxt = curr + i

        #         if nxt not in visited:
        #             visited.add(nxt)
        #             q.append((nxt, step + 1))

        # return -1
        end=0
        res=0
        maxi=0
        for i in range (len(nums)-1):
            maxi=max(maxi,i+nums[i])
            if i==end:
                res+=1
                end=maxi
        return res
