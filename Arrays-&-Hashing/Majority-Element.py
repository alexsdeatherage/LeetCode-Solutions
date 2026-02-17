# Input: List of integers
# Output: Integer, representing majority element
# Example: [2, 1, 3, 3, 3] -> 3
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Init hashmap to count integer freq in nums
        mElement = Counter(nums)
        # After for loop, return key with the highest val
        most_val = 0
        most_el = 0
        for k, v in mElement.items():
            if v > most_val:
                most_el = k
                most_val = v

        return most_el 