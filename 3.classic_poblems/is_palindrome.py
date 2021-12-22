# Copyright 2021 aaaaaaaalesha

from typing import Optional
from math import ceil


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def find_half(self, head: Optional[ListNode]) -> Optional[ListNode]:
    index = -1
    node = head
    while node is not None:  # O(N)
        node = node.next
        index += 1

    node = head
    for _ in range(ceil(index / 2)):  # O(N)
        node = node.next

    return node


def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    prev = head
    node = head.next

    prev.next = None

    while node.next is not None:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    head = node
    node.next = prev

    return head


def is_palindrome(self, head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return True

    back_reverse_node = self.reverse_list(self.find_half(head))  # O(N)

    node = head
    back_node = back_reverse_node

    while back_node is not None:  # O(N)
        if node.val != back_node.val:
            self.reverse_list(back_reverse_node)  # O(N)
            return False
        node = node.next
        back_node = back_node.next

    self.reverse_list(back_reverse_node)  # O(N)
    return True
