class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        class Node:
            def __init__(self, letter):
                self.val = letter
                self.parents = set()
                self.children = set()

        nodeMap = {}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]


            j = k = 0
            while j < len(word1) and k < len(word2):
                if word1[j] == word2[k]:
                    j += 1
                    k = j
                else:
                    break

            if j >= len(word1) or k >= len(word2):
                if not j >= len(word1):
                    return ""
                continue
            
            letter1 = word1[j]
            letter2 = word2[k]

            node1 = nodeMap.get(letter1, Node(letter1))
            node2 = nodeMap.get(letter2, Node(letter2))
            node1.children.add(node2)
            node2.parents.add(node1)

            nodeMap[letter1] = node1
            nodeMap[letter2] = node2

        start = []
        for node in nodeMap.values():
            if not node.parents:
                start.append(node)

        if not start and len(nodeMap) > 1:
                return ""
        
        invalid = False
        def dfs(curr, visited, currPath):
            nonlocal retVal
            nonlocal invalid

            currNode = nodeMap[curr]

            currPath += curr

            for node in currNode.children:
                if node.val in visited:
                    
                    invalid = True
                    return
                visited.add(node.val)
                dfs(node.val, visited, currPath)
                visited.remove(node.val)

            if len(currPath) > len(retVal):
                retVal = currPath


        
        
        totalVal = ""

        for node in start:
            visited = {node.val}
            retVal = ""
            dfs(node.val, visited, "")
            totalVal += retVal
            if invalid:
                return ""
                

        for word in words:
            for letter in word:
                if letter not in nodeMap:
                    totalVal = letter + totalVal
                    nodeMap[letter] = None
        
        return totalVal
        




     