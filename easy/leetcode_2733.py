class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        """
        Если длина массива меньше 3-х, то значения, которое не является максимальным и минимальным, не существует -> -1
        Для решения задачи достаточно 3-х любых элементов массива. Элемент со средним значением будет удовлетворять условию задачи
        """
        if len(nums) <= 2:
            return -1
        
        index_of_max = index_of_min = 0
        for i in range(1, 3):
            if nums[i] > nums[index_of_max]:
                index_of_max = i
                continue
            if nums[i] < nums[index_of_min]:
                index_of_min = i
                continue
        # Сумма всех индексов от 0 до 2 - 3. Находим незадействованный индекс
        return nums[3 - index_of_max - index_of_min]
            