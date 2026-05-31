# Beginner Friendly Add Two Numbers Solution
# Disclaimer
# This is a simple and beginner-friendly solution.
# The idea is to convert both linked lists into integers,
# add them together, then rebuild the resulting linked list.
# Approach
# Traverse the first linked list and reconstruct
# the integer it represents.
#
# Traverse the second linked list and do the same.
#
# Add both integers together.
#
# Extract every digit from the result and store them.
#
# Rebuild a linked list using the extracted digits
# in reverse order so it matches the required format.
#
# Return the final linked list.
# Complexity
# Time complexity:
# O(n + m)
# n = length of list1
# m = length of list2
#
# Space complexity:
# O(n + m)
#
# Additional space is used to store the digits
# before rebuilding the linked list.
# Solution Code
#
#
# python3
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lsum = 0
        l1Len = 0
        l1LenFinder = l1
        l2Len = 0
        l2LenFinder = l2
        while l1LenFinder:
            l1Len += 1
            l1LenFinder = l1LenFinder.next

        while l2LenFinder:
            l2Len += 1
            l2LenFinder = l2LenFinder.next

        for i in range(1, l1Len + 1):
            if l1:
                lsum += (l1.val * (10 ** i)) // 10
                l1 = l1.next

        for i in range(1, l2Len + 1):
            if l2:
                lsum += (l2.val * (10 ** i)) // 10
                l2 = l2.next

        sumReturn = None

        if lsum:
            sumLen = 0
            lsumStock = lsum
            while lsumStock != 0:
                lsumStock //= 10
                sumLen += 1

            rev = []
            lsumForRev = lsum
            for i in range(0, sumLen):
                rev.append(lsumForRev % 10)
                lsumForRev //= 10

            rev.reverse()
            lsum = rev
            i = 1
            nVal = 0
            sumReturn = ListNode(lsum[0])
            while True:
                if i < len(lsum):
                    nVal = lsum[i]
                    sumReturn = ListNode(nVal, sumReturn)
                    i += 1
                else:
                    break
        else:
            sumReturn = ListNode()

        return sumReturn
