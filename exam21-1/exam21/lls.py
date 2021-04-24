class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedListStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        Returns True if list is empty; False otherwise

        :return: bool
        """

    def push(self, item):
        """
        Pushes 'Node' item on top of stack

        :parameter:item: 'Node' being pushed
        :return: None
        """

    def pop(self):
        """
        Pops 'Node' off the top of the stack;
        throws error if stack is empty

        :return: Node
        """

    def peek(self):
        """
        Returns Node on top of stack without removing it;
        Returns None is stack is empty

        :return: Node
        """

    def size(self):
        """
        Returns the number of nodes that comprise the stack

        :return: int
        """
