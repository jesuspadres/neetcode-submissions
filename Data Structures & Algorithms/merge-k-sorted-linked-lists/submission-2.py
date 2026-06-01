# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        retVal = None
        curr = None

        while True:
            minimum = 1001
            minNode = None
            mIndex = -1
            for i, node in enumerate(lists):
                if node and node.val < minimum:
                    minimum = node.val
                    minNode = node
                    mIndex = i
            if not minNode:
                break
            elif not curr:
                retVal = minNode
                curr = minNode

            node2 = minNode.next
            lists[mIndex] = node2

            curr.next = minNode
            curr = curr.next

        return retVal

            
