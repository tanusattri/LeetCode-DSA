class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start=0
        size= len(arr)
        end= size-1
        if size==1:
            return 0
        while start<=end:
            mid= start+(end-start)//2
            if mid>0 and mid<size-1:
                if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                    return mid
                elif arr[mid-1]>arr[mid]:
                    end= mid-1
                else:
                    start= mid+1
            elif mid==0:
                if arr[0]>arr[1]:
                    return 0
                else:
                    return 1
            elif mid== size-1:
                if arr[size-1]>arr[size-2]:
                    return size-1
                else:
                    return size-2