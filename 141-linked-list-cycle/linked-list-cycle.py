# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        itr = head
        if itr==None:
            return False
        while itr.next != None:
            if itr.val == float('-inf'):
                return True
            itr.val = float('-inf')
            itr = itr.next
        return False