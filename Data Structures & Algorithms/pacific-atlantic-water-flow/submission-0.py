class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pa = set()
        at = set()

        def dfs(r,c, visited, prevHeight):
            if(r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            (r,c) in visited or
                heights[r][c] < prevHeight
            ):
                return 
            visited.add((r,c) )

            dfs(r-1,c,visited, heights[r][c])
            dfs(r,c-1,visited, heights[r][c])
            dfs(r+1,c,visited, heights[r][c])
            dfs(r,c+1,visited, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pa, heights[0][c])
            dfs(ROWS-1, c, at, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pa, heights[r][0])
            dfs(r, COLS-1, at, heights[r][COLS-1])
        
        both = pa & at
        return [[r,c] for r, c in both ]