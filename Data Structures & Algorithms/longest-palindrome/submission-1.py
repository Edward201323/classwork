class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        solution = 0
        odd_counted = False
        for key, value in counter.items():
            if odd_counted == False and value % 2 == 1:
                solution += value
                odd_counted = True
            elif value % 2 == 1:
                solution += value - 1
            else:
                solution += value
        
        return solution

        
