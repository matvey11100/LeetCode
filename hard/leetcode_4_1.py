class Solution:
    class Car:
        def __init__(self, a = 0, b = 0):
            self.a = -1000000
            self.b = -1000000
        def append(self, val):
            if self.a > self.b:
                self.b = val
            else:
                self.a = val
        def get(self):
            return max(self.a, self.b)
        def __str__(self):
            return f"a = {self.a}, b = {self.b}"


    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = len(nums1) + len(nums2)
        l1 = l
        flag = l1 % 2  # Четное ли общее количество элементов: True - нечетное, False - четное
        l1 = l1 // 2 + 1
        i = j = 0
        n = self.Car()
        while i < len(nums1) and j < len(nums2) and i + j < l1:
            if nums1[i] < nums2[j]:
                n.append(nums1[i])
                i += 1
            else:
                n.append(nums2[j])
                j += 1
        # Если один массив весь добавили, а второй еще нет, добавляем дальше
        while i < len(nums1) and i + j < l1:
            n.append(nums1[i])
            i += 1
        while j < len(nums2) and i + j < l1:
            n.append(nums2[j])
            j += 1
        if flag:
            return n.get()
        else:
            return (n.a + n.b) / 2         

sol = Solution()
nums1 = [1, 1, 2]
nums2 = [1, 3, 4]
print(f"nums1= {nums1}\nnums2= {nums2}")
print(sol.findMedianSortedArrays(nums1, nums2))