class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        position = (0, 0)
        for movement in path:
            if movement == 'N':
                position = (position[0], position[1] + 1)
            if movement == 'S':
                position = (position[0], position[1] - 1)
            if movement == 'E':
                position = (position[0] + 1, position[1])
            if movement == 'W':
                position = (position[0] - 1, position[1])
            
            if position in visited:
                return True
            else:
                visited.add(position)
            
        return False
