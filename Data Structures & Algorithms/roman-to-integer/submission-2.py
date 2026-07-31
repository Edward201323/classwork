class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000}

        solution = 0   
        for i in range(1, len(s)):
            curr = d[s[i - 1]]
            next = d[s[i]]
            if curr >= next:
                solution += curr
            else:
                solution -= curr
        
        solution += d[s[len(s) - 1]]
        return solution