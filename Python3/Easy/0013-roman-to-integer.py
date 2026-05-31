# Beginner Friendly Roman To Integer Solution

# Disclaimer
# This is a simple and beginner-friendly solution.
# The idea is to transform special Roman numeral cases
# into normal additive forms before calculating the total.

# Approach
# Create a dictionary that maps Roman numerals to integers.
#
# Replace subtractive combinations like:
# IV -> IIII
# IX -> VIIII
# so every character can simply be added.
#
# Iterate through the modified string and add every Roman numeral value to the final number.

# Complexity
# Time complexity:
#O(n)
#
# Space complexity:
#O(n)

# Solution Code
#
#
#python3
#
#1 <= s.length <= 15
#s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#It is guaranteed that s is a valid roman numeral in the range [1, 3999].
class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumbers = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        s = list(s)
        number = 0
        for i in range(0, len(s)):
            number += romanNumbers[s[i]]

        return number
