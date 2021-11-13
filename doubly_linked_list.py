# Copyright 2021 aaaaaaaalesha


class DoublyLinkedList:
    class Node:
        def __init__(self, value: int, ptr_next=None, ptr_prev=None):
            self.val = value
            self.next = ptr_next
            self.prev = ptr_prev

    def __init__(self):
        self.__head = None

    def get(self, index: int) -> int:
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

    def addAtHead(self, val: int) -> None:
        if self.__head is None:
            self.__head = DoublyLinkedList.Node(val)
            return

        node = DoublyLinkedList.Node(val, self.__head)
        self.__head = node

    def addAtTail(self, val: int) -> None:
        if self.__head is None:
            self.__head = DoublyLinkedList.Node(val)
            return

        node = self.__head

        while node.next is not None:
            node = node.next

        node.next = DoublyLinkedList.Node(val, None, node)

    def addAtIndex(self, index: int, val: int) -> None:
        if self.__head is None:
            if index == 0:
                self.__head = DoublyLinkedList.Node(val)
            return

        if index == 0:
            node = DoublyLinkedList.Node(val, self.__head)
            self.__head = node
            return

        prev_node = None
        node = self.__head
        for i in range(0, index):
            if node.next is None:
                if i == index - 1:
                    node.next = DoublyLinkedList.Node(val, None, node)
                return
            prev_node = node
            node = node.next

        prev_node.next = DoublyLinkedList.Node(val, node, prev_node)

    def deleteAtIndex(self, index: int) -> None:
        if self.__head is None:
            return

        if index == 0:
            self.__head = self.__head.next
            return

        prev_node = None
        node = self.__head
        for i in range(0, index):
            if node.next is None:
                return
            prev_node = node
            node = node.next

        prev_node.next = node.next
        if node.next is not None:
            node.next.prev = prev_node
