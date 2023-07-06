from queue import LifoQueue


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        if s[0] not in brackets:
            return False
        lifo_queue = LifoQueue(maxsize = 5000)
        
        for char in s:
            if char in brackets:
                lifo_queue.put(brackets[char])
            elif lifo_queue.qsize() == 0 or char != lifo_queue.get():
                return False

        if lifo_queue.qsize() != 0:
            return False
        return True

a = Solution()
s = "(){}}{"
print(a.isValid(s))

