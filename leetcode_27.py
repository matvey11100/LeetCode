class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

sol = Solution()
nums = [1, 1]
val = 0
print(sol.removeElement(nums, val), nums)Ы