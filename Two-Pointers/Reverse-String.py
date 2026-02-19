# Input: List of string characters, representing a single string s
# Output: None
# Example: s = ["b", "i", "g", "", "r", "e", d"] -> ["d", "e", "r", "", "g", "i", "b"]
# s = [], -> []
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # init l, r ptrs
        l, r = 0, len(s) - 1
        # while loop, l < r
        while l < r:
        # swap characters of l and r positioning
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        # return
        return