# Copyright 2021 aaaaaaaalesha

class LinkedList:
    class Node:
        def __init__(self, value: int, ptr_next=None):
            self.val = value
            self.next = ptr_next

    def __init__(self):
        self.__head = None

    def get(self, index: int) -> int:  # O(N)
        if self.__head is None:
            return -1

        if index == 0:
            return self.__head.val

        node = self.__head
        for _ in range(0, index):
            if node.next is None:
                return -1
            node = node.next

        return node.val

    def add_at_index(self, index: int, val: int) -> None:  # O(N)
        if self.__head is None:
            if index == 0:
                self.__head = LinkedList.Node(val)
            return

        if index == 0:
            node = LinkedList.Node(val, self.__head)
            self.__head = node
            return

        prev = None
        node = self.__head
        for i in range(0, index):
            if node.next is None:
                if i == index - 1:
                    node.next = LinkedList.Node(val)
                return
            prev = node
            node = node.next

        prev.next = LinkedList.Node(val, node)

    def add_at_head(self, val: int) -> None:  # O(1)
        self.add_at_index(0, val)

    def add_at_tail(self, val: int) -> None:  # O(N)
        if self.__head is None:
            self.__head = LinkedList.Node(val)
            return

        curr = self.__head

        while curr.next is not None:
            curr = curr.next

        curr.next = LinkedList.Node(val)

    def delete_at_index(self, index: int) -> None:  # O(N)
        if self.__head is None:
            return

        if index == 0:
            self.__head = self.__head.next
            return

        prev = None
        node = self.__head
        for i in range(0, index):
            if node.next is None:
                return
            prev = node
            node = node.next

        prev.next = node.next
