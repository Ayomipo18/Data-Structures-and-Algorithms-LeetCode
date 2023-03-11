/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    let currNode = head;
    while(currNode){
      if(currNode.next!=null && currNode.val===currNode.next.val){
        currNode.next = currNode.next.next
      } else currNode = currNode.next;
    }
    return head;
};