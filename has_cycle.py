# Copyright 2021 aaaaaaaalesha

from typing import Optional

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Floyd's tortoise and hare algorithm.
    Create two references to the head and move them at different speeds: 1 and 2.
        - If the linked list has a cycle they will definitely meet;
        - Else either of the two references(or their next) will become None.

    Time complexity: O(N).
    Space complexity: O(1).
    """
    if head is None:
        return False

    tortoise = head
    hare = head

    while tortoise is not None and hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next

        if tortoise is hare:
            return True

    return False
