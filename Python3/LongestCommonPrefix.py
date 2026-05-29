# Beginner Friendly Longest Common Prefix Solution

# Disclaimer
# This is a simple and beginner-friendly solution.
# The idea is to compare all strings vertically,
# character by character, until a difference is found.

# Approach
# Find the length of the shortest string.
#
# Compare the character at the same position
# in every string.
#
# If all characters are identical,
# add the character to the common prefix.
#
# If a difference is found,
# stop immediately and return the prefix found so far.
#
# If the loop finishes,
# return the complete common prefix.

# Complexity
# Time complexity:
# O(n * m)
# n = number of strings
# m = length of the shortest string
#
# Space complexity:
# O(m)

# Solution Code
#
#
# python3
#
#1 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lowercase English letters if it is non-empty.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        commonPrefix = []

        for i in range(0, len(min(strs, key=len))):
            valueStock = []
            for value in strs:
                value = list(value)[i]
                valueStock.append(value)
            if len(set(valueStock)) >= 2:
                break
            else:
                commonPrefix.append(valueStock[0])
                valueStock = []


        return "".join(commonPrefix)
