class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        y = x
        a = 0
        b = 0
        while y:
            
            b = y % 10
            a = a * 10 + b
            y //= 10
        print(a)
        return x == a


a = Solution()
print(a.isPalindrome(11))