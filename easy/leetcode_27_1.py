from collections import deque


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        k = 0
        queue = deque()  # Используем очередь для хранения индексов свободных элементов
        for i in range(len(nums)):
            if nums[i] == val:
                queue.append(i)  # Если элемент подлежит удалению, освобождаем индекс
            elif len(queue):
                nums[queue.popleft()] = nums[i]  # Если элемент не подлежит удалению и есть свободный индекс, переносим в свободный индекс
                queue.append(i)  # Также освобождаем предыдущий индекс элемента
                k += 1  
            else:
                k += 1
        
        return k

sol = Solution()
nums = [2, 1]
print(nums)
print(sol.removeElement(nums, 2), nums)