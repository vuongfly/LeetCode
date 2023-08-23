class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
        for j in dict_t:
            if dict_t[j] != dict_s.get(j, 0):
                return False
        return True


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
