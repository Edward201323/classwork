class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = {}
        for word in words:
            for char in word:
                counter[char] = counter.get(char, 0) + 1
        
        for value in counter.values():
            if value % len(words) != 0:
                return False
        
        return True