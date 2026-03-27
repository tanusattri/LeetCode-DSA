class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        if n==1: return nums[0]
        def sublinear(sub_nums):
            m= len(sub_nums)
            dp= [-1]*m
            def solve(i):
                if i>=m: return 0
                if dp[i]!=-1: return dp[i]
                take= sub_nums[i]+ solve(i+2)
                not_take= 0+solve(i+1)
                dp[i]= max(take, not_take)
                return dp[i]
            return solve(0)
        return max(sublinear(nums[:-1]), sublinear(nums[1:]))