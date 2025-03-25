# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = set()
        curr = head
        
        while curr:
            if curr.val in count:
                prev.next = curr.next
            else:
                count.add(curr.val)
                prev = curr
            curr = curr.next
        
        return head