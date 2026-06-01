# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 or curr2 or carry == 1:
            if curr1.next == None and curr2.next:
                curr1.next = ListNode()
            elif curr1.next and not curr2.next:
                curr2.next = ListNode()

            if curr1 and curr2:
                newVal = curr1.val + curr2.val + carry
                if newVal >= 10:
                    curr1.val = newVal%10
                    carry = 1
                else:
                    curr1.val = newVal
                    carry = 0

            if not curr1.next and not curr2.next and carry == 1:
                curr1.next = ListNode(1)
                break

            curr1 = curr1.next
            curr2 = curr2.next

        return l1