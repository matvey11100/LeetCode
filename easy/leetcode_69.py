class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, x // 2 + 2):
            temp = i * i
            if temp == x:
                return i
            elif temp > x:
                return i - 1