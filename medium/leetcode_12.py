class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dictionary = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }

        result = ""

        for key in sorted(dictionary, reverse=True):
            if num >= key:
                c = num // key
                result += dictionary[key] * c
                num -= key * c
                if num == 0:
                    return result




a = Solution()
print(a.intToRoman(1994))
print(a.intToRoman(58))