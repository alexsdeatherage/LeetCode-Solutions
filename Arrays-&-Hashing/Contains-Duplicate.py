from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        # Init Set
        dupe = set()
        # For n in nums: check if inside set, otherwise add to set
        for n in nums:
            if n in dupe:
                return True
            else:
                dupe.add(n)
        # If inside set, return True. Return False if outside loop
        return False