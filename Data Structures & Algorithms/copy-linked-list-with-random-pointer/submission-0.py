"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyhashmap = {None : None}
        current = head
        while current:
            copy = Node(current.val)
            copyhashmap[current] = copy
            current = current.next
        current = head
        while current:
            copy = copyhashmap[current]
            copy.next = copyhashmap[current.next]
            copy.random = copyhashmap[current.random]
            current = current.next
        return copyhashmap[head]