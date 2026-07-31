class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sol = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                sol += 1
        
        return sol