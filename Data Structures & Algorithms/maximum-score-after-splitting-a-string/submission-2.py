class Solution:
    def maxScore(self, s: str) -> int:
        scores = [0] * len(s)

        if s[0] == "0":
            scores[0] += 1
        for c in range(1, len(s)):
            if s[c] == "1":
                scores[0] += 1

        for i in range(1, len(s)):
            new_score = scores[i - 1]
            if s[i] == "0":        
                new_score += 1
            else:
                new_score -= 1
            scores[i] = new_score

        return max(scores)