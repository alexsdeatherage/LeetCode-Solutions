# Input: list of strings of lowercase English letters
# Output: List of lists, containing anagrams of strings
# Example: ["bed", "edd", "dde", ""] -> [["bed"], [""], ["edd", "dde"]]
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Init and words as defaultdict(list)
        words = defaultdict(list)
        # for loop in strs:
        for s in strs:
        # Init array [0] * 26 to count char freqs
            chars = [0] * 26
        # for loop for char in strs, add to array
            for c in s:
                diff = ord(c) - ord('a')
                chars[diff] += 1
        # add string to defaultdict
            words[tuple(chars)].append(s)
        # return values() of defaultdict
        return list(words.values())
        