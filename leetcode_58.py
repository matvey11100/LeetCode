class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0

        for char in reversed(s):
            if char != " ":
                count += 1
            elif count != 0:
                break
        return count
        
