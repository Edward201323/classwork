class Solution:
    def makeEqual(self, words: List[str]) -> bool:
            d = {}
            for word in words:
                for char in word:
                    d[char] = d.get(char, 0) + 1
            
            for value in d.values():
                if value % len(words) != 0:
                    return False

            return True
