# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr_node = head

        while curr_node:
            if curr_node not in visited:
                visited.add(curr_node)
            else:
                return True
            curr_node = curr_node.next

        return False