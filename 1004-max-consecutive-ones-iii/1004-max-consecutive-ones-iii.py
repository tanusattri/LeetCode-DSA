class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n= len(nums)
        i,j= 0,0
        max_length=0
        zeros_count=0
        while j<n:
            if nums[j]==0:
                zeros_count+=1
            if zeros_count<=k:
                max_length= max(max_length,j-i+1)
            else:
                if nums[i]==0:
                    zeros_count-=1
                i+=1
            j+=1
        return max_length