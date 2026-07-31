class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        largest_num = 0
        s = set()

        duplicate = -1
        for num in nums:
            if num > largest_num:
                largest_num = num
            
            if num in s:
                duplicate = num      
            else:
                s.add(num)

        missing_number = -1
        for i in range(1, len(nums) + 1):
            if i not in nums:
                missing_number = i
        
        if missing_number == -1:
            missing_number = len(nums)


        return [duplicate, missing_number]