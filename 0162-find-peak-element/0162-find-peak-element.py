class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start=0
        size= len(nums)
        end= size-1
        if size==1:
            return 0
        while start<=end:
            mid= start+(end-start)//2
            if mid>0 and mid<size-1:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                elif nums[mid-1]>nums[mid]:
                    end= mid-1
                elif nums[mid+1]>nums[mid]:
                    start= mid+1
            elif mid==0:
                if nums[0]>nums[1]:
                    return 0
                else:
                    return 1 
            elif mid== size-1:
                if nums[size-1]>nums[size-2]:
                    return size-1
                else:
                    return size-2