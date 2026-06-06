//
//Beginner Friendly Two Sum Solution
//
//Disclaimer
//This is a simple and beginner-friendly solution.
//The idea is to check every pair of numbers until the target is found.
//
//Approach
//Loop through the array.
//For each number, compare it with every other number.
//If the sum of two numbers equals the target, return their indices immediately.
//This solution is easy to understand, but not the fastest one.
//
//Complexity
//Time complexity:
//O(n²)
//
//Space complexity:
//O(1)
//
//Notes
//This solution focuses on clarity and understanding.
//A more advanced solution can use a hash map to improve performance.

//Solution Code
//
//
//c
//
//2 <= nums.length <= 104
//-109 <= nums[i] <= 109
//-109 <= target <= 109
//Only one valid answer exists.
//
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *result = malloc(2 * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        for (int index = 0; index < numsSize; index++) {
            if (i != index) {
                if (nums[i] + nums[index] == target) {
                    result[0] = i;
                    result[1] = index;
                    *returnSize = 2;
                    return result;
                }
            }
        }
    }
    *returnSize = 0;
    return 0;
}
