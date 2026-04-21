class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n= len(nums)
        i,j= 0,0
        curr_sum=0
        max_sum= float('-inf')
        while j<n:
            curr_sum+= nums[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                max_sum= max(max_sum, curr_sum)
                curr_sum-= nums[i]
                i+=1
                j+=1
        return max_sum/k