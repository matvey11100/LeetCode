class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not len(nums):
            return 0
        i = 0
        j = len(nums)
        while i != j:
            m = i + (j - i) // 2
            a = nums[m]
            if a == target:
                return m
            elif a > target:
                j = m
            else:
                i = m + 1
        return i
        
        
            
            

