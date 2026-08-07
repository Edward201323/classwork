class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        solutions = 0
        while True:
            if (counter['b'] >= 1 and counter['a'] >= 1 and counter['l'] >= 2 
            and counter['o'] >= 2 and counter['n'] >= 1):
                solutions += 1
            else:
                return solutions
            counter['b'] -= 1
            counter['a'] -= 1
            counter['l'] -= 2
            counter['o'] -= 2
            counter['n'] -= 1
            
            
                