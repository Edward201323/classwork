class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_counter = Counter(words[0])
        
        for word in words:
            compare = Counter(word)
            for key in char_counter.keys():
                if compare[key] < char_counter[key]:
                    char_counter[key] = compare[key]
        
        sol = []
        for key, value in char_counter.items():
            for i in range(value):
                sol.append(key)

        return sol

                

        