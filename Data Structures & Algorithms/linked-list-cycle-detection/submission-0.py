# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = {}
        node = head
        while node:
            if nodes.get(node,0) != 0:
                return True
            else:
                nodes[node] = 1
            node = node.next

        return False