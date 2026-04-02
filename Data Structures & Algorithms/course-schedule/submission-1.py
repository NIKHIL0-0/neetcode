from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        dic = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        # FIX 1: reverse graph direction
        for cr, pre in prerequisites:
            dic[pre].append(cr)   # pre → cr
            indegree[cr] += 1

        q = deque()

        # initial nodes with indegree 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            c = q.popleft()
            count += 1   # FIX 2: increment here

            for nei in dic[c]:   # FIX 3: use c, not i
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return count == numCourses