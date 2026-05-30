# Beginner Friendly Merge Two Sorted Lists Solution

# Disclaimer
# This is a simple and beginner-friendly solution.
# The idea is to convert both linked lists into a Python list,
# sort all values, then rebuild a new linked list.

# Approach
# Traverse the first linked list and store every value.
#
# Traverse the second linked list and store every value.
#
# Sort all collected values.
#
# Build a new linked list from the sorted values.
#
# Return the head of the newly created linked list.

# Complexity
# Time complexity:
# O((n + m) log(n + m))
# n = number of nodes in list1
# m = number of nodes in list2
#
# Space complexity:
# O(n + m)

# Notes
# This solution focuses on simplicity and understanding.
# It does not take advantage of the fact that both linked
# lists are already sorted. A more advanced solution can
# merge the lists directly without sorting again.

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
#
#
#The number of nodes in both lists is in the range [0, 50].
#-100 <= Node.val <= 100
#Both list1 and list2 are sorted in non-decreasing order.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = []
        if list1 != None:
            current = list1
            while current:
                sortedList.append(current.val)
                current = current.next

        if list2 != None:
            current = list2
            while current:
                sortedList.append(current.val)
                current = current.next

        if sortedList:
            sortedList.sort(reverse=True)
            current = ListNode(sortedList[0])
            i = 1
            while current:
                if i <= len(sortedList) - 1:
                    current = ListNode(sortedList[i], current)
                else:
                    break

                i += 1
        else:
            return None

        return current

