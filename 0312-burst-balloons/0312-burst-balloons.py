class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr= [1]+ nums+ [1]
        n= len(arr)
        dp= [[-1 for _ in range(n)] for _ in range(n)]
        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]
            ans= 0
            for k in range(i,j+1):
                temp_ans= solve(i,k-1)+ solve(k+1,j)+ (arr[i-1]*arr[k]*arr[j+1])
                ans= max(ans,temp_ans)
            dp[i][j]= ans
            return ans
        return solve(1,len(nums))