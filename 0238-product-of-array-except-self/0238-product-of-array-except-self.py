class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        answer= [1]*n
        for i in range(1,n):
            answer[i]= nums[i-1]*answer[i-1] #store left elements multiplication 
        suffix_product=1
        for i in range(n-1,-1,-1):
            answer[i]= answer[i]*suffix_product #store right elements multiplication 
            suffix_product*= nums[i]
        return answer