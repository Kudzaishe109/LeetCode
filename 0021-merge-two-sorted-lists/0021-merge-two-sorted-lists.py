# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_one = list1
        curr_two = list2
        dummy = ListNode()
        curr = dummy
        while curr_one and curr_two:
            if curr_one.val <= curr_two.val:
                curr.next = ListNode(curr_one.val)
                curr_one = curr_one.next
            else: 
                curr.next = ListNode(curr_two.val)
                curr_two = curr_two.next
            curr = curr.next
        while curr_one:
            curr.next = ListNode(curr_one.val)
            curr_one = curr_one.next
            curr = curr.next

        while curr_two:
            curr.next = ListNode(curr_two.val)
            curr_two = curr_two.next
            curr = curr.next

        return dummy.next





        