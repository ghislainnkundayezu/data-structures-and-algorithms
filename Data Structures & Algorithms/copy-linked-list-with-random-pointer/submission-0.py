"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy 

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}

        curr_node = head
        while curr_node:
            node_map[curr_node] = Node(curr_node.val)
            curr_node = curr_node.next
        
        curr_node = head
        while curr_node:
            new_node = node_map[curr_node]
            new_node.next = node_map[curr_node.next]
            new_node.random = node_map[curr_node.random]

            curr_node = curr_node.next

        return node_map[head]