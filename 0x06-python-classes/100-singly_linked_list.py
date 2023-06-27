#!/usr/bin/python3
"""Singly linked list and Node implementation"""


class Node:
    """A node of a singly linked list"""
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int) or value is None:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""
    def __init__(self) -> None:
        self.__head = None

    def sorted_insert(self, value):
        """inserts a node into the linked list"""
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
            return
        current_node = self.__head
        if new_node.data < self.__head.data:
            new_node.next_node = current_node
            self.__head = new_node
            return
        next_node = current_node.next_node
        while next_node is not None:
            if current_node.data <= new_node.data and \
              next_node.data >= new_node.data:
                new_node.next_node = next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
            next_node = next_node.next_node
        current_node.next_node = new_node

    def __str__(self) -> str:
        """defines the string representation of the sll"""
        sll_string = ""
        current_node = self.__head
        while current_node.next_node is not None:
            sll_string += f"{current_node.data}\n"
            current_node = current_node.next_node
        sll_string += f"{current_node.data}"
        return sll_string
