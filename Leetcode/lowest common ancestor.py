class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def LCA(self, root:Node, p:Node, q:Node):
        curr=root
        while curr:
            if p.val > curr.val and q.val > curr.val:
              curr=curr.right
            elif p.val < curr.val and q.val < curr.val:
              curr=curr.left
            else:
              return curr