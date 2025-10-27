# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        middle, prev_middle = None, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev_middle
            prev_middle = curr
            curr = next_node
        tail = prev_middle
        curr_fhead, curr_ftail = head, tail
        while curr_ftail:
            if curr_ftail.val != curr_fhead.val:
                return False
            curr_ftail, curr_fhead = curr_ftail.next, curr_fhead.next
        return True
        

        