# Copyright 2021 aaaaaaaalesha

from typing import Optional

def get_intersection(self, head_a: Optional[ListNode], head_b: Optional[ListNode]) -> Optional[ListNode]:
    """
    We need to find a way to line up the ends of the two lists. To concatenate them in opposite orders, A+B and B+A
    This way, the ends of the two original lists will align on the second half of each merged list.
    """
    if head_a is None or head_b is None:
        return None

    ptr_a = head_a
    ptr_b = head_b

    while ptr_a is not ptr_b:
        ptr_a = ptr_a.next if ptr_a is not None else head_b
        ptr_b = ptr_b.next if ptr_b is not None else head_a

    return ptr_a
