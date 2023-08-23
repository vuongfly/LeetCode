import collections
from typing import List


class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            print(*count)
            print(s)
            ans[tuple(count)].append(s)
        return ans.values()

    def groupAnagrams(self, strs: List[str]):
        anagram_map = collections.defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


# Create an instance of the Solution class
solution = Solution()

# Test the function with different inputs
strs = ["eat","tea","tan","ate","nat","bat"]
strs_2 = [""]
result1 = solution.groupAnagrams(strs)
result2 = solution.groupAnagrams(strs_2)

print("Result 1:", result1)  # [["bat"],["nat","tan"],["ate","eat","tea"]]
print("Result 2:", result2)  # [[""]]
