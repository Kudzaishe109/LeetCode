# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (head.next == None and n ==1):
            return None
            
        count_nodes = 0
        curr = head
        while curr:
            count_nodes += 1
            curr = curr.next
        
        index = count_nodes - n 
        if index <= 0:
            return head.next
        curr = head
        i = 0
        while curr.next and i < index - 1:
            curr = curr.next
            i += 1

        curr.next = curr.next.next
        return head
        
        