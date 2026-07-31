class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        occurences = Counter(magazine)
        for char in ransomNote:
            if not occurences.get(char) or occurences[char] == 0:
                return False
            if occurences[char]:
                occurences[char] -= 1
        
        return True