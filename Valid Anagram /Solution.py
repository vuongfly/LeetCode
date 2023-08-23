class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        d = {"a": 3, "b": 2}
        d1 = {"b": 2, "a": 3}
        res = all((d1.get(k) == v for k, v in d.items()))
        return res

# Create an instance of the Solution class
solution = Solution()

# Test the function with different inputs
test_input1 = "abc"
test_input2 = "bca"
test_input3 = "abc"
test_input4 = "def"

result1 = solution.isAnagram(test_input1, test_input2)
result2 = solution.isAnagram(test_input3, test_input4)

print("Result 1:", result1)  # Expected output: True
print("Result 2:", result2)  # Expected output: False