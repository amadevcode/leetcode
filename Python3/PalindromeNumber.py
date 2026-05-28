# Beginner Friendly Palindrome Number Solution

# Disclaimer
# This is a simple digit-based solution. It reconstructs the reversed number
# using arithmetic operations (no string conversion). It is mainly for learning
# purposes and understanding number manipulation.

# Approach
# First, handle negative numbers (they cannot be palindromes).
#
# Then, determine the number of digits in the number.
#
# Iterate through each digit from right to left:
# - Extract the last digit using modulo 10
# - Build the reversed number by placing digits in correct position
#   using powers of 10
#
# Finally, compare the reconstructed number with the original.

# Complexity
# Time complexity:
# O(n) where n is the number of digits
#
# Space complexity:
# O(1)

# Solution Code


#Without converting the integer to a string
#-231 <= x <= 231 - 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        xlen = 0
        xlenX = x

        while xlenX > 0:
            xlenX //= 10
            xlen += 1

        rev = x
        num = 0

        for i in range(1, xlen + 1):
            num += (rev % 10) * 10 ** (xlen - i)
            rev //= 10


        return x == num
