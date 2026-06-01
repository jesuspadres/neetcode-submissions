# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        retVal = head = None

        while True:
            smallest = float('inf')
            idx = -1
            for i in range(len(lists)):
                curr = lists[i]

                if curr:
                    if curr.val < smallest:
                        smallest = curr.val
                        idx = i
            if idx == -1:
                break
            elif retVal == None:
                retVal = head = ListNode(smallest)
            else:
                head.next = ListNode(smallest)
                head = head.next

            lists[idx] = lists[idx].next

        return retVal