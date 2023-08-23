from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        preSet = set()
        for num in nums:
            if num in preSet:
                return True
            preSet.add(num)
        return False;

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         #if set of nums == nums length each val diff
#         return len(set(nums))!=len(nums)

solution = Solution()
test_input1 = [1, 2, 3, 4, 5]
test_input2 = [1, 2, 3, 2, 4]

result1 = solution.containsDuplicate(test_input1)
result2 = solution.containsDuplicate(test_input2)

print("Result 1:", result1)  # Expected output: False
print("Result 2:", result2)  # Expected output: True