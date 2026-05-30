# Beginner Friendly Remove Duplicates from Sorted Array Solution

# Disclaimer
# This solution works but is not optimal.
# It uses a copy of the array and removes duplicates during iteration.
# A more advanced solution uses the two-pointer technique and modifies
# the array in-place without extra space.

# Approach
# Create a copy of the original array.
#
# Iterate through the copy and compare adjacent elements.
#
# If two consecutive elements are equal,
# remove the duplicate from the original array.
#
# Return the modified array implicitly via LeetCode requirements.

# Complexity
# Time complexity:
# O(n^2) due to repeated removals in a list.
#
# Space complexity:
# O(n) because of the extra copied array.

# Notes
# This solution is intended for learning purposes and understanding
# how duplicates appear in a sorted array. It is not optimal.

# Solution Code
#
#
# python3
#
#1 <= nums.length <= 3 * 104
#-100 <= nums[i] <= 100
#nums is sorted in non-decreasing order.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsPosition = nums.copy()
        for i in range(0, len(nums) - 1):
            if i < len(numsPosition) - 1:
                if numsPosition[i + 1] == numsPosition[i]:
                    nums.remove(numsPosition[i])
