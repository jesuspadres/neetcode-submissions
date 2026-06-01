"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return 
        nodesList = []
        nodesMap = {}
        randomMap = {}
        copyNodes = []

        curr = head
        i = 0
        while curr:
            nodesList.append(curr)
            nodesMap[curr] = i
            copyNodes.append(Node(curr.val))

            i += 1
            curr = curr.next

        curr = head
        while curr:
            rand = curr.random
            if rand:
                randIdx = nodesMap[rand]
                randomMap[curr] = randIdx
            curr = curr.next

        for i in range(len(copyNodes)):
            node = nodesList[i]
            if i+1 < len(copyNodes):
                copyNodes[i].next = copyNodes[i+1]

            if node not in randomMap:
                continue
            randIdx = randomMap[node]
            copyNodes[i].random = copyNodes[randIdx]
            

        return copyNodes[0]