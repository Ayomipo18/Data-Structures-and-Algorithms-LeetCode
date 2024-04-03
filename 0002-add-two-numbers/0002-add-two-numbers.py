# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - while we have l1.val or l2.val or carry > 0
        - add l1, l2 and carry value
        - If l1 value is null, make it zero
        - if l2 value is null, make it zero
        - Also, if l1.next doesn't exist, don't move
        - Also, if l2.next doesn't exist, don't move
        - time - O(max(len(l1, l2)))
        - time - O(max(len(l1, l2)))
        '''
        carry = 0
        result = ListNode()
        ans = result
        
        while l1 or l2 or carry > 0:
            l1_val = 0 if l1 == None else l1.val
            l2_val = 0 if l2 == None else l2.val
            
            val = l1_val + l2_val + carry
            
            carry = int(val / 10)
            val = int(val % 10)
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result.next = ListNode(val)
            result = result.next
            
        return ans.next