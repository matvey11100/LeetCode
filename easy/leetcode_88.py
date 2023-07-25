class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = m - 1  # Указатель первого массива
        j = m + n - 1  # Второй указатель первого массива
        k = n - 1  # Указатель второго массива

        while k >= 0:
            
            if nums1[i] > nums2[k] and i >= 0:
                nums1[j] = nums1[i]
                i -= 1
            else:
                nums1[j] = nums2[k]
                k -= 1
            j -= 1
            print(nums1, i, k)



nums1 = [1,4,6,0,0,0,0]
nums2 = [2,5,7,8]
m = 3
n = 4
sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)
