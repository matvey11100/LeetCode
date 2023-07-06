class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l = len(nums1) + len(nums2)
        l1 = l
        flag = l1 % 2  # Четное ли общее количество элементов: True - нечетное, False - четное
        l1 = l1 // 2 + 1
        n = []
        i = j = k = 0
        while i < len(nums1) and j < len(nums2) and k < l1:
            k += 1
            if nums1[i] < nums2[j]:
                n.append(nums1[i])
                i += 1
            else:
                n.append(nums2[j])
                j += 1
        # Если один массив весь добавили, а второй еще нет, добавляем дальше
        while i < len(nums1) and k < l1:
            k += 1
            n.append(nums1[i])
            i += 1
        while j < len(nums2) and k < l1:
            k += 1
            n.append(nums2[j])
            j += 1
        print(f"n = {n}, l1 = {l1}, flag = {flag}")
        if flag:
            return n[-1]
        else:
            return (n[-1] + n[-2]) / 2
            
            

sol = Solution()
nums1 = []
nums2 = [2, 3]
print(f"nums1= {nums1}\nnums2= {nums2}")
print(sol.findMedianSortedArrays(nums1, nums2))