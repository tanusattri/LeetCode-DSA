class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        prefix_sum=0
        count=0
        counts= {0:1}
        for num in nums:
            prefix_sum+= num
            if prefix_sum-k in counts:
                count+= counts[prefix_sum-k]
            counts[prefix_sum]= counts.get(prefix_sum,0)+1
        return count