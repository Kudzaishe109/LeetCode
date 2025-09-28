# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        store = []
        curr = head
        while curr:
            store.append(curr.val)
            curr = curr.next
        curr = ListNode(store.pop())
        head = curr
        while store:
            curr.next = ListNode(store.pop())
            curr = curr.next 
        return head





        