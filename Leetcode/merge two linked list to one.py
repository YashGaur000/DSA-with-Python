# class Listnode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergelist(self, l1:Listnode, l2:Listnode)->Listnode:
#         curr = dummy = Listnode()
#         print(dummy.next)
#         print(dummy.val)
#         while l1 and l2:
#             if l1.val < l2.val:
#                 curr.next = l1
#                 while curr.next:
#                     print(curr.val, end=" -> ")
#                     curr = curr.next
#                 l1 = l1.next
#             else:
#                 curr.next = l2
#                 l2 = l2.next
#             curr = curr.next

#         if not l1:
#             curr.next =l2
#         else:
#             curr.next = l1

#         return dummy.next

# solution = Solution()
# l1 = Listnode(1)
# l1.next = Listnode(2)
# l1.next.next = Listnode(3)

# # Create l2: 1 -> 4 -> 5
# l2 = Listnode(1)
# l2.next = Listnode(4)
# l2.next.next = Listnode(5)

# # Call the mergeList method
# result = solution.mergelist(l1, l2)
# while result:
#     print(result.val, end=" -> ")
#     result = result.next

class Listnode:
    def __init__(self, val=0 ,next=None):
        self.val = val
        self.next = next

class Solution():
    def mergelist(self, l1: Listnode, l2: Listnode) -> Listnode:
        