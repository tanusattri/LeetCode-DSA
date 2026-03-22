class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        max_sum=0
        curr_sum=0
        left=0
        window_set= set()
        for right in range(n):
            while nums[right] in window_set:
                window_set.remove(nums[left])
                curr_sum-= nums[left]
                left+=1
            window_set.add(nums[right])
            curr_sum+= nums[right]
            if right-left+1>k:
                window_set.remove(nums[left])
                curr_sum-= nums[left]
                left+=1
            if right-left+1==k:
                max_sum= max(max_sum, curr_sum)
        return max_sum