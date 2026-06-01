# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLen(head)

        if n == length:
            tmp = head.next
            head.next = None
            return tmp

        prev = head
        curr = head.next
        i = length - n
        while i > 0:
            i -= 1
            if i == 0:
                prev.next = curr.next
                curr.next = None
            else:
                prev = prev.next
                curr = curr.next

        return head        

    def getLen(self, head: Optional[ListNode]):
        n = 0

        curr = head
        while curr:
            n += 1
            curr = curr.next

        return n