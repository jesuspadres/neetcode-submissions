# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        listNodes = []

        curr = head
        while curr:
            listNodes.append(curr)
            curr = curr.next

        l = 0
        r = len(listNodes)-1

        for i in range(len(listNodes)):
            if l >= r: break

            listNodes[l].next = listNodes[r]
            l += 1

            if l >= r: break
            
            listNodes[r].next = listNodes[l]
            r -= 1

        listNodes[l].next = None

