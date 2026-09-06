# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        tail = dummy_node

        remainder = 0
        while l1 or l2 or remainder:
            n1, n2 = l1.val if l1 else 0, l2.val if l2 else 0


            curr_sum = remainder + n1 + n2
            remainder = curr_sum // 10
            new_node = ListNode(curr_sum%10)
            tail.next = new_node
            tail = new_node

            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        
        curr_node = l1 if l1 else l2


        return dummy_node.next
            
             
            