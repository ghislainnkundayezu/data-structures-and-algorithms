# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, curr_node: Optional[ListNode], prev_node=None) -> Optional[ListNode]:
 
        if curr_node == None:
            return prev_node

        temp_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = temp_node
        
        return self.reverseList(curr_node, prev_node)
             
