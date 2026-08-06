class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            prev = ord(s[i - 1])
            curr = ord(s[i])
            score += abs(prev - curr)
        return score
            