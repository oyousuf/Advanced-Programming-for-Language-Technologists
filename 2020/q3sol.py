# Node class:
class Node:
    def __init__(self, data, skip, next):
        self.next = next
        self.data = data
        self.skip = skip


# List class
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        strg = ''
        while current:
            strg = strg + '(' + current.data + ',' + str(current.skip) + ')'
            current = current.next
        return strg

    def insert(self, data, skip):
        self.head = Node(data, skip, self.head)

    def insert_list(self, data):
        if len(data) > 0:
            self.insert(data[0][0],data[0][1])
            self.insert_list(data[1:])

    def printSkip(self):
        current = self.head
        step = 0
        skip = 1
        while current:
            step += 1
            if step == skip:
                print(current.data)
                step = 0
                skip = current.skip
            current = current.next


    def removeValue(self, value):
        while self.head and self.head.data == value:
            self.head = self.head.next
        if self.head:
            current = self.head
            while current.next:
                if current.next.data == value:
                    current.next = current.next.next
                else:
                    current = current.next


ll = LinkedList()
ll.insert_list([("a", 3),("aaaa",6),("a",1),("e",6),("aaa", 3),("aa",1),("b",5),("a",2)])
print(ll)
ll.printSkip()

ll2 = LinkedList()
ll2.insert_list([("aaaaa", 1),("aaaa",1),("a",4),("e",6),("aaa", 3),("c",1),("aa",2),("a",1)])
print(ll2)
ll2.printSkip()

ll = LinkedList()
ll.insert_list([("a", 3),("g",6),("a",1),("e",6),("d", 3),("c",1),("b",5),("a",2)])
ll2 = LinkedList()
ll2.insert_list([("a", 3),("g",6),("a",1),("e",6),("d", 3),("c",1),("b",5),("a",2)])

ll.removeValue("a")
s1 = str(ll)
print(s1 == "(b,5)(c,1)(d,3)(e,6)(g,6)", s1)

ll.removeValue("b")
s2 = str(ll2)
print(s2 == "(a,2)(b,5)(c,1)(d,3)(e,6)(a,1)(g,6)(a,3)", s2)

