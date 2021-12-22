# Copyright 2021 aaaaaaaalesha

from typing import Optional

def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
