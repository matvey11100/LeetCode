class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, len(digits)):
                    digits[j] = 0
                break
        else:
            # Число состоит из девяток
            digits[0] = 1
            for i in range(1, len(digits)):
                digits[i] = 0
            digits.append(0)
        return digits