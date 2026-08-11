class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n= len(nums)
        seen= set(nums)
        total_sum= nums[0]
        for i in range(1,n):
            if nums[i]== nums[i-1]+1:
                total_sum+= nums[i]
            else:
                break
        while total_sum in seen:
            total_sum+=1
        return total_sum