# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - go through both lists and compare each current nodes, which ever is higher, put in the result and move the node in the list
        space - O(list1 + list2)
        time - O(List1 + list2)
        '''
        
        dummy = ListNode()
        result = dummy
        
        while list1 or list2:
            val1 = list1.val if list1 else 1000
            val2 = list2.val if list2 else 1000
            
            if val1 <= val2 :
                dummy.next = ListNode(list1.val)
                list1 = list1.next if list1 else None
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next if list2 else None

            dummy = dummy.next
            
        return result.next