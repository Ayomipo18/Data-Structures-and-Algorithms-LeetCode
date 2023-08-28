# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        - go through both lists and compare each current nodes, which ever is higher, put in the result and move the node in the list
        space - O(list1.length + list2.length)
        time - O(list1.length + list2.length)
        '''
        
        dummy = ListNode()
        result = dummy
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
                
            dummy = dummy.next
            
        if list1 or list2:
            dummy.next = list1 if list1 else list2
            
        return result.next