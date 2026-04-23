class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        for i in range(n - 1, 0, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
        for i in range(n - 1):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, (n - 1) - i)
                break
        return max_dist