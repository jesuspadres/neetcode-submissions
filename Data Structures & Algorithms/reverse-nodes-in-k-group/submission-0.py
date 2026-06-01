# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        length = self.lenList(head)
        curr = head
        head = None
        tail = None
        
        for i in range(0, length, k):
            
            if length - i >= k:
                a, b = self.reverseList(curr, k)
                if not head:
                    head = a
                else:
                    tail.next = a
                tail = b
            else:
                if not head:
                    head = curr
                else:
                    tail.next = curr
                break
            curr = tail.next

        return head
            
        

    def reverseList(self, head, k):
        prev = None
        tail = curr = head
        post = curr.next

        
        while post and k >= 1:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
            k -= 1
        tail.next = post

        return (prev, tail)

    def lenList(self, head):
        i = 0
        while head:
            head = head.next
            i += 1

        return i