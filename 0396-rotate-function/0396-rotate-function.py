class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n= len(nums)
        total_sum=0
        f=0
        for i in range(n):
            total_sum+= nums[i]
            f+= i*nums[i]
        result= f
        for k in range(1,n):
            f= f+total_sum-n*nums[n-k]
            result= max(result,f)
        return result 