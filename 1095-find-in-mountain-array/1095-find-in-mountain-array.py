class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        start = 0
        size = mountainArr.length()
        end = size - 1
        peakidx = -1
        while start <= end:
            mid = start + (end - start) // 2
            if mid > 0 and mid < size - 1:
                mid_val = mountainArr.get(mid)
                prev_val = mountainArr.get(mid - 1)
                nxt_val = mountainArr.get(mid + 1)
                if mid_val > nxt_val and mid_val > prev_val:
                    peakidx = mid
                    break 
                elif prev_val > mid_val:
                    end = mid - 1
                else:
                    start = mid + 1
            elif mid == 0:
                if mountainArr.get(0) > mountainArr.get(1):
                    peakidx = 0
                else:
                    peakidx = 1
                break
            elif mid == size - 1:
                if mountainArr.get(size - 1) > mountainArr.get(size - 2):
                    peakidx = size - 1
                else:
                    peakidx = size - 2
                break
        def binarySearchAsc(start, end):
            while start <= end:
                mid = start + (end - start) // 2
                mid_val = mountainArr.get(mid) 
                if target == mid_val:
                    return mid
                elif target < mid_val:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        def binarySearchDesc(start, end):
            while start <= end:
                mid = start + (end - start) // 2
                mid_val = mountainArr.get(mid)
                if target == mid_val:
                    return mid
                elif target < mid_val:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        left_res = binarySearchAsc(0, peakidx)
        if left_res != -1:
            return left_res
        return binarySearchDesc(peakidx + 1, size - 1)