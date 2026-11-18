class Solution:
    def climbStairs(self, n: int) -> int:
        # dp n = n -1 + n-2

        memo = {}
        def dfs(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2
            
            if n in memo:
                return memo[n]
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]
        return dfs(n)
