class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd_palindrome = False
        length = 0
        for value in counter.values():
            if value % 2 == 1:
                odd_palindrome = True
                length += value - 1
            else:
                length += value

        if odd_palindrome:
            return length + 1
        else:
            return length