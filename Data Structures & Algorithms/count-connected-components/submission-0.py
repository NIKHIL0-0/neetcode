class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range (n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen=set()
        def dfs(c,seen,adj):
            q=deque()
            q.append(c)
            seen.add(c)
            while q:
                cur=q.pop()
                
                for nei in adj[cur]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        count=0
        for i in adj:
            if i not in seen:
                count+=1
                dfs(i,seen,adj)
        return count

        