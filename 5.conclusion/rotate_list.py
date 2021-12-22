# Copyright 2021 aaaaaaaalesha
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def get_list_size(head: Optional[ListNode]) -> int:
        curr = head
        size = 0
        while curr is not None:
            curr = curr.next
            size += 1

        return size

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        size = self.get_list_size(head)

        # Normalize offset.
        k = k % size

        if k == 0:
            return head

        # Let's find node which will be last in resulted list.
        future_last_node = head
        for _ in range(size - k - 1):
            future_last_node = future_last_node.next

        end_node = future_last_node
        while end_node.next is not None:
            end_node = end_node.next

        end_node.next = head
        new_head = future_last_node.next
        future_last_node.next = None

        return new_head
