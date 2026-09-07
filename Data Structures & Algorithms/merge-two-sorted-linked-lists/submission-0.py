# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l = list1
        cur_r = list2
        cur = ListNode()
        new_list = cur

        while cur_l and cur_r:
            if cur_l.val < cur_r.val:
                cur.next = cur_l
                cur = cur.next
                cur_l = cur_l.next
            else:
                cur.next = cur_r
                cur = cur.next
                cur_r = cur_r.next
        
        cur.next = cur_l if cur_l else cur_r

        return new_list.next