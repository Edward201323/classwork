class Solution:
    def maxScore(self, s: str) -> int:
        max = 0
        for i in range(1, len(s)):
            l_score = 0
            for left in range(0, i):
                if s[left] == "0":
                    l_score += 1
            
            r_score = 0
            for right in range(i, len(s)):
                if s[right] == "1":
                    r_score += 1

            total = l_score + r_score
            if total > max:
                max = total

        return max 