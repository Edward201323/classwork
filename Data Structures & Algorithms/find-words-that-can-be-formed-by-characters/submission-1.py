class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0

        chars_counter = Counter(chars)
        for word in words:
            needed = Counter(word)
            valid = True
            for key, value in needed.items():
                if value > chars_counter[key]:
                    valid = False
            if valid:
                length += len(word)
            
        return length