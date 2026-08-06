class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for key, value in counter.items():
            if value == 1:
                return key

        return -1

        
