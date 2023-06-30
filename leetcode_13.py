class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary_1 = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        dictionary_2 = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        l = [dictionary_1, dictionary_2]

        result = 0
        temp = ''

        while s:
            temp = s[0:2]
            if temp not in dictionary_2:
                temp = s[0]
            i = len(temp)
            result += l[i - 1][temp]
            s = s[i:]
        
        return result
                

a = Solution()
print(a.romanToInt("MCMXCIV"))