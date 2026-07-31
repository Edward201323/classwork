class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0

        if s[0] == "0":
            max_score += 1
        for c in range(1, len(s)):
            if s[c] == "1":
                max_score += 1

        prev_score = max_score
        for i in range(1, len(s) - 1):
            new_score = prev_score
            if s[i] == "0":        
                new_score += 1
            else:
                new_score -= 1

            prev_score = new_score
            if new_score > max_score:
                max_score = new_score

        return max_score