# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        def build(root, soFar):
            if not root:
                return ""
            
            return soFar + str(root.val) + "," + build(root.left, soFar+"l,") + build(root.right, soFar+"r,")

        r = build(root, "")
        print(r)
        return r
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        root = TreeNode(int(data[0]))
        data = data.split(",")

        i = 1
        currNode = root
        while i < len(data)-1:
            curr = data[i]
            next = data[i+1]

            if curr == "l":
                if next != "l" and next != "r":
                    print(int(next))
                    currNode.left = TreeNode(int(next))
                    currNode = root
                    i += 2
                else:
                    currNode = currNode.left
                    i += 1
            elif curr == "r":
                if next != "l" and next != "r":
                    print(int(next))
                    currNode.right = TreeNode(int(next))
                    currNode = root
                    i += 2
                else:
                    currNode = currNode.right
                    i += 1

        return root

#"1,l2,r3,rl4,rr5"