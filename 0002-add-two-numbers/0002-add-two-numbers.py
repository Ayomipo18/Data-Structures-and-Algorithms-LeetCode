# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        result = root
        excess = 0
        while l1 or l2 or excess:
            if l1:
                excess += l1.val
                l1 = l1.next
            if l2:
                excess += l2.val
                l2 = l2.next
            
            result.next = ListNode(excess%10)
            result = result.next
            excess = excess//10
            
        return root.next 
#         carry = 0
#         pointer1 = l1
#         pointer2 = l2
#         result = ListNode()
        
#         while pointer1 != None or pointer2 != None:
#             new_val = pointer1.val + pointer2.val + carry
#             result.val = new_val if new_val < 10 else new_val % 10
#             carry = new_val // 10
#             pointer1 = pointer1.next
#             pointer2 = pointer2.next
#             result.next = ListNode()
#             result = result.next
            
#         while pointer1 != None:
#             new_val = pointer1.val + carry
#             result.val = new_val if new_val < 10 else new_val % 10
#             carry = new_val // 10
#             pointer1 = pointer1.next
#             result.next = ListNode()
#             result = result.next
            
#         while pointer2 != None:
#             new_val = pointer2.val + carry
#             result.val = new_val if new_val < 10 else new_val % 10
#             carry = new_val // 10
#             pointer2 = pointer2.next
#             result.next = ListNode()
#             result = result.next
            
#         result.val = carry if carry > 1 else result.val
#         return result