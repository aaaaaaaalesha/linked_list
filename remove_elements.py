# Copyright 2021 aaaaaaaalesha

from typing import Optional

def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head is not None and head.val == val:
        head = head.next

    if head is None:
        return head

    if head.next is None:
        if head.val == val:
            return None
        return head

    prev = head
    node = head.next

    while node is not None:
        if node.val == val:
            prev.next = node.next
            node.next = None
            node = prev.next
            continue

        node, prev = node.next, prev.next

    return head
