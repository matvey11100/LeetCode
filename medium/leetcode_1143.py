class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Создадим таблицу с нулевыми значениями со сторонами l1 + 1, l2 + 1, где l1 и l2 - длины поступивших на вход строк
        В заполненной таблице значение каждого поля [i][j] будет соответсвовать длине максимальной общей подпоследовательности
        строк text1[0 : i] и text2[0 : j]
        Первая колонна и строка - служебные, их значения не меняются
        Заполнение таблицы происходит слева-направо сверху-вниз, с поля [1][1] до поля [l1][l2]
        Если text[i] == text[j], то берем предыдущую максимальную подпоследовательность (table[i][j]) и прибавляем 1
        Иначе максимальная подпоследовательность не увеличивается и будет равна max(rectangle[i][j + 1], rectangle[i + 1][j])
        """

        table = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    table[i + 1][j + 1] = table[i][j] + 1
                else:
                    table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
        
        return table[len(text1)][len(text2)]




                
