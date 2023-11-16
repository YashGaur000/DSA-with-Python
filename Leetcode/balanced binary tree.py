class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isbalanced(self, root: [TreeNode]) -> bool:    
        def dfs(root):
            if not root: return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            print(left, right)
            balanced =(left[0] and right[0] and
                       abs(left[1] - right[1]) <= 1)
            # print(left[0], right[0], abs(left[1] - right[1]))
            return [balanced, 1+max(left[1], right[1])]
        return dfs(root)
    

# Creating the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.left.left.left = TreeNode(7)

# Creating an instance of the Solution class
solution = Solution()

# Calling the isbalanced method with the root node
result = solution.isbalanced(root)

print("Result returned by dfs for the root node:", result)


    