class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Given two binary strings a and b, return their sum as a binary string.

        """

        index = 0
        if len(a) < len(b):
            a, b = b, a
        result = ''
        remainder = 0

        while index < len(b):
            t1, t2 = map(int, (a[-1 - index], b[-1 - index]))
            temp, remainder = self.summ(t1, t2, remainder)
            result = str(temp) + result
            index += 1
        
        while index < len(a):
            t1 = int(a[-1 - index])
            temp, remainder = self.summ(t1, 0, remainder)
            result = str(temp) + result
            index += 1

        if remainder:
            result = str(remainder) + result

        return result
    
    def summ(self, x, y, remainder):
        res = x + y + remainder
        remainder = res // 2
        res %= 2
        return res, remainder


a = '111'
b = '11'
sol = Solution()
print(sol.addBinary(a, b))


