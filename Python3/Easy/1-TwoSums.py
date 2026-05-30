# Beginner Friendly Two Sum Brute Force Solution

# Disclaimer
# This is a simple brute force solution.
# It checks every possible pair until it finds the one that matches the target.

# Intuition
# Try all pairs of numbers and see whether their sum is equal to the target.

# Approach
# Use two nested loops to compare each number with every other number.
# Skip comparing a number with itself.
# If the sum of two numbers equals the target, return their indices immediately.

# Complexity
# Time complexity:
# O(n^2)
#
# Space complexity:
# O(1)

#Solution Code
#
#
#python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(0, len(nums)):
            for i in range(0, len(nums)):
                if i != index:
                    if nums[index] + nums[i] == target:
                        indexes = [index, i]
                        return indexes
