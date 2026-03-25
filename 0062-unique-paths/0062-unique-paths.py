class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i,j=0,0
        dp= [[-1 for _ in range(n)] for _ in range(m)]
        def solve(i,j)->int:
            if i==m-1 or j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            right= solve(i,j+1)
            down= solve(i+1,j)
            dp[i][j]= right+down
            return dp[i][j]
        return solve(0,0)