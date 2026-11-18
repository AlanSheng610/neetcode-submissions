class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return 
            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count