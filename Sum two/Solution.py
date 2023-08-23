from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}  # val : index
        for index, value in enumerate(nums):
            diff = target - value
            if diff in preMap:
                return [preMap[diff], index]
            preMap[value] = index
        return
