from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Init dictionary representing diff between target and nums[i]
        hashMap = dict()
        # use for loop to interate through nums
        for i in range(len(nums)):
        # take diff = target - nums[i]
            diff = target - nums[i]
        # if diff in dictionary, return i and associated index
            if diff in hashMap:
                return [hashMap[diff], i]
        # put key, value into dict as (nums[i], index)
            else:
                hashMap[nums[i]] = i
