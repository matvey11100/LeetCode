class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return 1

        index_to_move = 1
        a = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > a:
                nums[index_to_move] = nums[i]
                a = nums[i]
                index_to_move += 1
        
        return index_to_move

                



nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)
sol = Solution()
print(sol.removeDuplicates(nums))
print(nums)

