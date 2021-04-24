from sortarray import *


def instertion_sort(sa):
    for index in range(1, sa.getSize()): #start from 1 because a list with one item in position 0 is already sorted
        pos = index
        while pos > 0 and sa.cmp(pos-1, pos) >0: #compare the items between the two indices
            sa.swap(pos, pos-1) #the items are swaped if the above statement is true
            pos = pos - 1 #change the position if the above statement is not true



debug = False

sa = SortArray()
for size in range(10, 51, 10):
    print ("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print ("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print ("before: ")
            sa.printList()
        
        instertion_sort(sa)

        if debug:
            print ("after: ")
            sa.printList()

        sa.printInfo()
    
    print()


