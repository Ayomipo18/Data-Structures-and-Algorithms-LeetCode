# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - go through the length of the linkedlist
        - add two numbers
        - if there's a remainder, add it to carry else don't add it to carry
        - there might a remainder and some values from the linkedlist, so basically try to add those remainders
        '''
        
        carry = 0
        dummy = ListNode()
        result = dummy
        
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            new_val = val1 + val2 + carry # 5+4 or 5+7
            carry = new_val // 10
            new_val %= 10
            dummy.next = ListNode(new_val)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next
            
        return result.next