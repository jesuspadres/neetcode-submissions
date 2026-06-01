# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next

        index = length - n

        if index == 0:
            return head.next

        prev = head
        curr = head.next
        count = 1

        while curr:
            try:
                if count == index:
                    prev.next = curr.next
                    curr = curr.next.next
                else:
                    curr = curr.next
                prev = prev.next
                count += 1
            except:
                break

        return head