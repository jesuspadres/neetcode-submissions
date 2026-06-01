# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        back = None
        while slow:
            tmp = slow.next
            slow.next = back
            back = slow
            slow = tmp

        mid = back
        curr = head
        while mid and curr:
            tmp1 = curr.next
            tmp2 = mid.next
            curr.next = mid
            mid.next = tmp1
            curr = tmp1
            mid = tmp2

