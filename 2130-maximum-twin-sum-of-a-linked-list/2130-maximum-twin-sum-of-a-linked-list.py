# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        n = len(vals)
        ans = 0
        for i in range(n // 2):
            ans = max(ans, vals[i] + vals[n - 1 - i])
        return ans
        