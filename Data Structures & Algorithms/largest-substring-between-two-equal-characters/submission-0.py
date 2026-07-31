class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        visited = {}
        longest = -1
        for i in range(len(s)):
            char = s[i]
            if char not in visited:
                visited[char] = i
            else:
                substring_length = i - visited[char] - 1
                if substring_length > longest:
                    longest = substring_length
                    
        return longest