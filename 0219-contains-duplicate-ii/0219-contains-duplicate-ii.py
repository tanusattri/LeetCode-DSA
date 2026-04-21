class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n= len(nums)
        i,j=0,0
        window= set()
        while j<n:
            if nums[j] in window:
                return True
            window.add(nums[j])
            if j-i<k:
                j+=1
            else:
                window.remove(nums[i])
                i+=1
                j+=1
        return False