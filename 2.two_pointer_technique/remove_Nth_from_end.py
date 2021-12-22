# Copyright 2021 aaaaaaaalesha

from typing import Optional

def remove_Nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return head

    prev_n = head
    node = head

    for _ in range(n):
        node = node.next
        if node is None:
            head = head.next
            return head

    while node.next is not None:
        node, prev_n = node.next, prev_n.next

    prev_n.next = prev_n.next.next
    return head
