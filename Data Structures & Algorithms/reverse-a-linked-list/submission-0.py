# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        
        first = head
        second = head.next
        head.next = None
        while second is not None:
            temp = second.next
            second.next = first
            first = second
            second = temp

        return first
        
        