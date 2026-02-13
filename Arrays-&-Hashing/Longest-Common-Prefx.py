from typing import List
#Input: list[str]
#Output: str, longest common prefix of all strings

#Examples:
#Input: ["aba", ""]
#Output: ""

#Input: ["abab", "aba"]
#Output: "aba"

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # init result string
        result = ""
        # for loop, len(strs[0])
        for i in range(len(strs[0])):
        # for loop, s in strs
            for s in strs:
        # if s[i] != strs[0][i]. check if len(s) == i, return result
                if len(s) == i or s[i] != strs[0][i]:
                    return result
        # append s[i] to result
            result += s[i]
        # return result, out of for loop
        return result