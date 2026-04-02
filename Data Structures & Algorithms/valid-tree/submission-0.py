class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = {i : [] for i in range (n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        seen=set()
        def dfs(i,prev):
            if i in seen:
                return False
            seen.add(i)
            for nei in adj[i]:
                if nei==prev:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        return dfs(0,-1) and len(seen)==n
        
