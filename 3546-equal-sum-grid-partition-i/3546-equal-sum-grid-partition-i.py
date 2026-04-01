class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        current_row_sum = 0
        for i in range(m - 1):
            current_row_sum += row_sums[i]
            if current_row_sum == target:
                return True
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
        current_col_sum = 0
        for j in range(n - 1):
            current_col_sum += col_sums[j]
            if current_col_sum == target:
                return True
        return False