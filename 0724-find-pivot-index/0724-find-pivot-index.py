class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n= len(nums)
        total_sum=0
        for i in range(n):
            total_sum+= nums[i]
        cs=0
        for i in range(n):
            ls= cs
            rs= total_sum- ls- nums[i]
            if ls==rs:
                return i
            else:
                cs+= nums[i]
        return -1