# Beginner Friendly Longest Substring Without Repeating Characters Solution

# Disclaimer
# This is a simple and beginner-friendly solution.
# The idea is to keep a current substring with no repeated characters
# and expand it while updating it whenever a duplicate is found.

# Approach
# Iterate through the string character by character.
#
# Keep track of the characters currently in the substring.
#
# If the current character is not already in the current substring,
# add it.
#
# If the current character is already present,
# remove characters from the start of the current substring
# until the repeated character is removed.
#
# After processing the whole string,
# return the maximum length found.

# Complexity
# Time complexity:
# O(n^2)
#
# Space complexity:
# O(n)

# Solution Code
#
#
# python3
#
#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sChar = list(s)
        seenChar = []
        streak = []
        for char in sChar:
            if char not in seenChar:
                seenChar.append(char)
            else:
                streak.append(len(seenChar))
                del seenChar[:seenChar.index(char) + 1]
                seenChar.append(char)




        streak.append(len(seenChar))
        return max(streak)
