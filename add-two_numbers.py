# Copyright 2021 aaaaaaaalesha
from typing import Optional


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Given two non-empty linked lists.
    highest_digit = 1 if l1.val + l2.val > 9 else 0
    result_list = ListNode((l1.val + l2.val) % 10)
    l1, l2 = l1.next, l2.next
    nodes_builder = result_list

    while l1 is not None and l2 is not None:
        nodes_builder.next = ListNode((highest_digit + l1.val + l2.val) % 10)
        highest_digit = 1 if highest_digit + l1.val + l2.val > 9 else 0
        l1, l2 = l1.next, l2.next
        nodes_builder = nodes_builder.next

    l1 = l2 if l2 is not None else l1

    while l1 is not None:
        nodes_builder.next = ListNode((highest_digit + l1.val) % 10)
        highest_digit = 1 if highest_digit + l1.val > 9 else 0
        l1 = l1.next
        nodes_builder = nodes_builder.next

    if highest_digit != 0:
        nodes_builder.next = ListNode(highest_digit)

    return result_list
