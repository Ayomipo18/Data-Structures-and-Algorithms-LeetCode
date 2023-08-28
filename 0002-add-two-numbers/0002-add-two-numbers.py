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
        pointer1 = l1
        pointer2 = l2
        result = ListNode()
        dummy = result
        
        while pointer1 != None or pointer2 != None or carry:
            v1 = pointer1.val if pointer1 != None else 0
            v2 = pointer2.val if pointer2 != None else 0
            new_val = v1 + v2 + carry
            result.next = ListNode(new_val) if new_val < 10 else ListNode(new_val % 10)
            carry = new_val // 10
            pointer1 = pointer1.next if pointer1 != None else None
            pointer2 = pointer2.next if pointer2 != None else None
            result = result.next
            
        return dummy.next