# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = ListNode(0)
        curr1 = head1
        curr = head.next
        node_val = 0
        while curr:
            if curr.val == 0:
                curr1.next = ListNode(node_val)
                curr1 = curr1.next
                node_val = 0
            else:
                node_val += curr.val
            curr = curr.next
        return head1.next

        