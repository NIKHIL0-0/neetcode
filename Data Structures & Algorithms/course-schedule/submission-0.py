from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic={i:[] for _ in range (numCourses)}
        inorder=[0]*(numCourses-1)
        for cr,pre in prerequisites:
            dic[cr].append(pre)
            inorder[cr]+=1
        q=deque()
        for i in range (numCourse):
            if inorder[i]==0:
                q.append(i)
        count=0
        seen=set()
        while q:
            c=q.popleft()
            for i in dic[i]:
                inorder[i]-=1
                if inorder[i]==0:
                    q.append(i)
                    count+=1
        return count==numCourses
                


