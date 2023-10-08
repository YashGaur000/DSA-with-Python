class Listnode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def mergelist(self, l1: Listnode, l2: Listnode) -> Listnode:
        curr = dummy = Listnode()
        while l1 and l2:
            if l1.value < l2.value:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if not l1:
            curr.next = l2
        else:
            curr.next = l1

        return dummy.next


solution = Solution()
l1 = Listnode(1)
l1.next = Listnode(2)
l1.next.next = Listnode(3)

l2 = Listnode(1)
l2.next = Listnode(2)
l2.next.next = Listnode(3)

result = solution.mergelist(l1, l2)

while result:
    print(result.value, end=' -> ')
    result = result.next



