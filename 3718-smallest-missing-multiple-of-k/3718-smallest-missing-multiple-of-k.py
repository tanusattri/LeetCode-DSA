class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        if k not in nums:
            return k
        for i in range(len(nums)):
            c= (i+2)*k
            if c not in nums:
                return c 