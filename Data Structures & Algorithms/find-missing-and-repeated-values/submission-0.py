class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid)
        visited = set()
        expected = set()
        for i in range(1, length * length + 1):
            expected.add(i)

        duplicate = -1
        for row in range(length):
            for col in range(length):
                curr = grid[row][col]
                if curr in expected:
                    expected.remove(curr)
                if curr in visited:
                    duplicate = curr
                else:
                    visited.add(curr)

        return [duplicate, expected.pop()]
