class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [-1]*n
        def solve(i)-> int:
            if i>=n:
                return 0
            if  dp[i]!=-1:
                return dp[i]
            take= nums[i]+solve(i+2)
            not_take= 0+solve(i+1)
            dp[i]= max(take,not_take)
            return dp[i]
        return solve(0)