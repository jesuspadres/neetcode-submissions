# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverseHead = None

        curr = head
        while curr:
            newNode = ListNode(curr.val, reverseHead)
            reverseHead = newNode

            curr = curr.next

        curr = head
        while curr:
            if curr.val != reverseHead.val:
                return False

            curr = curr.next
            reverseHead = reverseHead.next

        return True