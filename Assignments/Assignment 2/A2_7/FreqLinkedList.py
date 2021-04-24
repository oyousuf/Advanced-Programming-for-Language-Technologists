

class Node:
    def __init__(self, word, next):
        self.next = next
        self.word = word
        self.freq = 1


class FreqLinkedList:
    def __init__(self):
        self.head = Node("**dummy**", None)

    def addWord(self, word):
        new_node = Node(word, None)
        if word < self.head.word:
            self.head = Node(word, self.head)
        else:
            current = self.head
            while current.next and word >= current.next.word:
                current = current.next
            if word == current.word:
                current.freq += 1
            else:
                current.next, new_node.next = new_node, current.next

    def printList(self):
        node = self.head.next
        while node:
            print(node.word, node.freq)
            node = node.next

    def filterWords(self, limit):
        current = self.head
        while current.next:
            node = current.next
            if node.freq < limit:
                current.next = node.next
            else:
                current = current.next

