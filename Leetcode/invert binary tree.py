class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        

class Solution:
    def invertTree(self, root: Node) -> Node:
        if not root:
            return root
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
solution = Solution()
n1 = Node(1)
# n1.left = Node(2)
# n1.right = Node(3)

# n1.left.left = Node(4)
# n1.left.right = Node(5)
# n1.right.left = Node(6)
# n1.right.right = Node(7)

result = solution.invertTree(n1)
while result:
    print(result.val, end=' -> ')
    result = result.left







