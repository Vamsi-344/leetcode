# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getTheNumber(self, ll: Optional[ListNode]) -> int:
        count = 0
        if ll == None:
            return count
        itr = ll
        res = 0
        while itr.next:
            res += (itr.val)*(10**(count)) 
            itr = itr.next
            count += 1
        res += (itr.val)*(10**(count)) 
        return res
    
    def createAList(self, s: int) -> Optional[ListNode]:
        ll = ListNode(int(s[0]), None)
        itr = ll
        for i in s[1:]:
            itr.next = ListNode(int(i), None)
            itr = itr.next
        return ll


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.getTheNumber(l1)
        b = self.getTheNumber(l2)
        c = a + b
        d = str(c)
        e = d[::-1]
        return self.createAList(e)