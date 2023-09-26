#!/usr/bin/python3
"""creating a linked list using inheritance"""


class Node:
    def __init__(self, data, next_node=None):
        """ Initiates a class Node
            Args:
                data (int): data to be stored in a node
                next_node (Node): Node that created a linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ value (int): data to be stored in a node """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ value (Node): Node to create a linked list """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """ Initiates a class SinglyLinkedList
            Args:
                None
        """
        self.head = None

    def sorted_insert(self, value):
        """ adds a new node to the list end"""
        newnode = Node(value, None)
        if self.head is None:
            self.head = newnode
        elif self.head.data > newnode.data:
            newnode.next_node = self.head
            self.head = newnode
        else:
            temp = self.head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            newnode.next_node = temp.next_node
            temp.next_node = newnode

    def __str__(self):
        """ Returns a string representation of the linked list. """
        lists = []
        temp = self.head
        while temp:
            lists.append(str(temp.data))
            temp = temp.next_node
        return "\n".join(lists)
