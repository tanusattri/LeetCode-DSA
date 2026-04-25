class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev= int(str(n)[::-1])
        ans= abs(n-rev)
        return ans 