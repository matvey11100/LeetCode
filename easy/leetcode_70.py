class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a, b = 1, 2
        for i in range(3, n + 1):
            temp = b
            b = a + b
            a = temp
        
        return b
    

sol = Solution()
for n in range(1, 100):
    res = sol.climbStairs(n)
    print(f"n = {n}; res = {res}")


