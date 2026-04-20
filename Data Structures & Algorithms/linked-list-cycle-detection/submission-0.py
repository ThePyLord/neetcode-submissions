# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        is_cycle = False

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                is_cycle = True
                break
        return is_cycle