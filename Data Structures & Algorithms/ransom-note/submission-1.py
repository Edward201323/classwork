class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = {}
        for char in magazine:
            magazine_freq[char] = magazine_freq.get(char, 0) + 1
        
        ransom_freq = {}
        for char in ransomNote: 
            ransom_freq[char] = ransom_freq.get(char, 0) + 1
        
        for key, val in ransom_freq.items():
            if not magazine_freq.get(key) or magazine_freq.get(key) < val:
                return False
        
        return True