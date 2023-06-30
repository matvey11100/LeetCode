class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenght = len(nums)

        for i in range(lenght):
            for j in range(i + 1, lenght):
                if nums[i] + nums[j] == target:
                    return i, j
        

