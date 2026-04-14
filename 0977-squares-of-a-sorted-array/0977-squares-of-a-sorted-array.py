class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n= len(nums)
        square= []
        for i in range(n):
            ans= nums[i]*nums[i]
            square.append(ans)
            i+=1
        square.sort()
        return square  