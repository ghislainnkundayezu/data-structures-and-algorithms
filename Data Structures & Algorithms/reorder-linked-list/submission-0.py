# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list into two portions
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None

        # reverse the right linked hand of the linked list
        prev = None
        curr = middle

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # now we are adding the elements in that respective order
        left, right = head, prev
         
        dummy_node = ListNode()
        curr_node = dummy_node

        while left and right:
            temp_left = left.next
            temp_right = right.next

            curr_node.next = left
            curr_node = left 
            curr_node.next = right
            curr_node = right

            left = temp_left
            right = temp_right

 
        if left:
            curr_node.next = left

         


