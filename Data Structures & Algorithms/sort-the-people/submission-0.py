class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]

        heights.sort(reverse = True)

        sol = []

        for height in heights:
            sol.append(d[height])
        
        return sol