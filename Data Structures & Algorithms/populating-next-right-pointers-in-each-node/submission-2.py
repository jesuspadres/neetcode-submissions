"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        nullNode = 1
        count = 0

        queue = deque([root])

        while queue:
            count += 1
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if nullNode == count:
                node.next = None
                nullNode *= 2
                count = 0
            else:
                node.next = queue[0]

        return root



            