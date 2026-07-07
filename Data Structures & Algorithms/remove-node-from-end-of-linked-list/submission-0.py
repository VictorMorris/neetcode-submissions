# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Loop for number of nodes
        node = head
        nodeCnt = 1
        while node:
            node = node.next
            nodeCnt += 1
        # Remove len-nth node
        nodeIdx = 1
        prevNode, currNode, nextNode = None, head, head.next

        while currNode:
            if nodeIdx == nodeCnt-n:
                if prevNode:
                    prevNode.next = None
                    currNode.next = None
                    if nextNode:
                        prevNode.next = nextNode
                else:
                    head = nextNode
                return head
            else:
                nodeIdx += 1
                prevNode = currNode
                currNode = nextNode
                if nextNode:
                    nextNode = nextNode.next
                else:
                    nextNode = None

        return head

