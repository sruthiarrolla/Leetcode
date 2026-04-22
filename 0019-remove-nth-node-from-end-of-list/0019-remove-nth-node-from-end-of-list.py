# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy
        f=s=dummy
        for i in range(n):
            f=f.next
        while f.next:
            s=s.next
            f=f.next
        s.next=s.next.next
        return dummy.next
        