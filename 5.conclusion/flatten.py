# Copyright 2021 aaaaaaaalesha
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def descend(self, parent: Node, child: Node) -> Node:
        parent_next = parent.next

        # Re-link pointers.
        parent.next = child
        child.prev = parent
        parent.child = None

        node = parent
        while node.next is not None or node.child:
            if node.child is not None:
                node = self.descend(node, node.child)
                continue

            node = node.next

        node.next = parent_next
        if parent_next is not None:
            parent_next.prev = node

        return node

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr is not None:
            if curr.child is not None:
                # If curr has a child, let's descend and flatten levels.
                curr = self.descend(curr, curr.child)

            curr = curr.next

        return head
