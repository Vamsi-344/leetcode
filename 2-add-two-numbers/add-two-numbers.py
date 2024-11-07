# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def liValue(self, l: Optional[ListNode]) -> int:
        count, res, itr = 0, 0, l
        while itr.next != None:
            res += (itr.val*(10**(count)))
            count += 1
            itr = itr.next
        res += itr.val*10**(count)
        return res
    
    def numToLinkedList(self, x: int) -> Optional[ListNode]:
        head = None
        temp = head
        for i in str(x):
            temp = ListNode(int(i))
            temp.next = head
            head = temp
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        req = self.liValue(l1) + self.liValue(l2)
        return self.numToLinkedList(req)

        