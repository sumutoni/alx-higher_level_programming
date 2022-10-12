#!/usr/bin/python3
"""
A node class to define node of a singly linked list,
and a singly linked list class
"""


class Node:
    """Node class to define a node of linked list"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Singly linked class"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts node in increasing order"""
        if self.__head is None:
            self.__head = Node(value, None)
            return
        else:
            self.__cur = self.__head
            self.__prev = None
            while (self.__cur is not None and self.__cur.data < value):
                self.__prev = self.__cur
                self.__cur = self.__cur.next_node
            if (self.__cur is None):
                self.__cur = Node(value, None)
                self.__prev.next_node = self.__cur
                return
            if (self.__cur.data > value):
                if (self.__cur == self.__head):
                    self.__prev = Node(value, self.__cur)
                    self.__head = self.__prev
                    return
                else:
                    self.__prev.next_node = Node(value, self.__cur)

    def __str__(self):
        """Method to print data of instance"""
        self.__cur = self.__head
        res = ""
        while self.__cur is not None:
            res += "{:d}\n".format(self.__cur.data)
            self.__cur = self.__cur.next_node
        return res
