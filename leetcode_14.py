class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        result = strs[0]

        for i in range(1, len(strs)):
            string = strs[i]
            if len(result) > len(string):
                result = result[:len(string)]
            for j in range(len(result)):
                if result[j] != string[j]:
                    result = result[:j]
                    break
        
        return result
    

a = Solution()
input = ["ab", "a"]
print(a.longestCommonPrefix(input))
