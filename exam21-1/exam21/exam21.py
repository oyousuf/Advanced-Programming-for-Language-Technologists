"""

This is the answer sheet for the Advanced Programming, Spring 2021 final exam.
Use these multiline comment blocks to answer questions, whether they are
formatted as short answers or open-ended. Where code is provided, you can edit
it directly in-line. Submit this file exactly as its formatted to Studium when
you are done.

"""

###########################################################################
# # # # # # # # # # # # # # # Q U E S T I O N 1 # # # # # # # # # # # # # #
###########################################################################

from random import randint


class TerrainRace:
    def __init__(self, terrain, debug=False):
        self.terrain = terrain
        self._pos = 0
        self.debug = debug

    def _move(self):
        move_length, move_strength = self._random_move_parameters()
        if self.debug:
            self._show_position(move_length, move_strength)
        while (self._pos < len(self.terrain)
               and move_length
               and move_strength >= self.terrain[self._pos]):
            move_length -= 1
            self._pos += 1

    def _random_move_parameters(self):
        return randint(1, 6), randint(1, 6)

    def _show_position(self, d1, d2):
        for i, t in enumerate(self.terrain):
            if self._pos == i:
                print('*', end='')
            else:
                print(' ', end='')
            print(t, end='')
        print(f'   {d1} {d2}')

    def number_of_moves(self):
        self._pos = 0
        counter = 0
        while self._pos < len(self.terrain):
            counter += 1
            self._move()
        return counter

    def ave_number_of_moves(self, tries=10000):
        total = 0
        for _ in range(tries):
            total += self.number_of_moves()
        return total/tries

#c
class HardTerrainRace(TerrainRace):
    def _move(self):
        move_length, move_strength = self._random_move_parameters()
        if self.debug:
            self._show_position(move_length, move_strength)
        while (self._pos < len(self.terrain)
               and move_length
               and move_strength >= self.terrain[self._pos]):
            move_length -= 1
            self._pos += 1
            if move_length == 0:
                self._pos -= 1

#b
class SingleDieTerrainRace(TerrainRace):

    def _move(self):
        move_length = self._random_move_parameters()
        move_strength = move_length
        if self.debug:
            self._show_position(move_length, move_strength)
        while (self._pos < len(self.terrain) and move_length and move_strength >= self.terrain[self._pos]):
            move_length -= 1
            self._pos += 1

    def _random_move_parameters(self):
        return randint(1, 6)


###########################################################################
# # # # # # # # # # # # # # # Q U E S T I O N 2 # # # # # # # # # # # # # #
###########################################################################

"""

A. O(nm^2) - the first for loop is the array x so that's going to be variable n,
the next for loop is array y so that's going to be m and inside that one has another
for loop traversing through the same array y, this will be another m. the inner-most 
for loop is going to have a constant of 1/2 yielding a more accurate big O as O(n*(m^2/2),
but that 1/2 constant doesn't matter, so we're left with n(m^2)

B. O(nm) - the top for loop is going over array x (variable n). the outer for loop below is
going over the same, n, while the inner for loop is going over array y (variable m). the more
accurate big O, I suppose is O(n+nm) / factored out as O(n(1+m)), but the nm is a higher order so we don't care about 
the lone n.

C. O(mlogn) - the while loop is traversing over array x (variable n) and the for loop is traversing
array y (variable m). But the while loop has n = n//2 which will give it a logarithmic complexity,
making it log n. so in total we have mlogn

D. O(m^3) - this one has all 3 for loops traversing through the same array, array y (as variable m).
this yields m^3. the statements in the inner-most for loop with reassigning the array doesn't add to the 
complexity.

"""

###########################################################################
# # # # # # # # # # # # # # # Q U E S T I O N 3 # # # # # # # # # # # # # #
###########################################################################

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        # will see if there's nothing in the first node/head
        if self.head is None:
            return True
        else:
            return False
        """
        Returns True if list is empty; False otherwise

        :return: bool
        """

    def push(self, item):
        # What I'm doing is under the assumption I got from
        # the instructions which is that the newest node
        # created will be sent to the end of the linked list.
        # The wording threw me off a bit.

        if self.head is None:
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        self.count += 1
        """
        Pushes 'Node' item on top of stack

        :parameter:item: 'Node' being pushed
        :return: None
        """

    def pop(self):
        # can call isEmpty method instead of rewriting same
        # conditionals to check if the linked list is empty
        if self.isEmpty():
            return 'Error'
        else:
            delNode = self.head
            self.head = self.head.next
            delNode.next = None
            self.count -= 1
            return delNode.data
        """
        Pops 'Node' off the top of the stack;
        throws error if stack is empty

        :return: Node
        """

    def peek(self):
        # do same isEmpty check first as before
        if self.isEmpty():
            return None
        # just return the top node's data as it'll be the
        # self.head here
        else:
            return self.head.data
        """
        Returns Node on top of stack without removing it;
        Returns None is stack is empty

        :return: Node
        """

    def size(self):
        return self.count
        """
        Returns the number of nodes that comprise the stack

        :return: int
        """

###########################################################################
# # # # # # # # # # # # # # # Q U E S T I O N 4 # # # # # # # # # # # # # #
###########################################################################

"""

Write your answer here.

I would use 1 outer dictionary as my main access point to the rest of the data. I believe this will work with the caveat
that the telecommunications company has either a finite number of rankings, or if they come up with a new ranking then 
update the dictionary with it, as you'll see later on.
The length of the dictionary, meaning the number of keys minus 1, would be predetermined by the number of rankings the
telecommunications company has. So if they have rankings 1,2,3,4, and 5 then the the keys of the dictionary would be the
same, (1,2,3,4,5). Next the values of these keys would be structured with singly linked lists, with the self.head in
each singly linked list constantly being updated wth the customer next in line. The linked list will be filled out in
order of first come first serve FOR SPECIFICALLY THAT RANKING, not just for ALL customers with varying rankings. And
just as the example presented in the instructions portrayed, if there are two customers in rank 3 (which is the highest
ranking defined by the telecommunications company), one customer with rank 2, and one customer with rank 1 then the 
operators will be give both customers in rank 3 priority over the customers with rank 2 and 1, and the customers with
rank 3 will be dealt with in order of which called in first, as customers are added to the tails of linked lists as they
come in.
Operations of storing data and printing are as follows:
customers with ranking are fed into the dictionary and their ranking is matched against the dictionary's keys, then the 
customer is added to the tail-end of the linked list corresponding to that specific key. Now, once a customer is taken
care of, in any linked list, they are removed as the self.head of that linked list and the self.head.next is assigned as
the new self.head, continuously updating as callers are dealt with or if they drop from the call. All customers in the 
highest priority ranking (in this case rank 3) must be dealt with before allocating representatives to lesser rankings.
This can be accomplished with a simple isEmpty() method, commonly made in linked list classes (or even from the previous
question in this exam), for the highest ranking key's value's linked list.
For time complexities:
Insertion and deletion of nodes in the singly linked list both have average and worst case time complexities of O(1)
which is nice for this example. The dictionary's time complexity on average is O(1) as well as it functions as a hashmap
in python, requiring the inner parameters to be has functions. This is advantageous as other times collisions can occur
and it'd make the worst time complexity be O(n). Next, the operation of the previously mentioned isEmpty() method to 
check if the higher ranking's linked list has customer waiting is a constant. All in all, I think this is a 
semi-efficient solution with a minimized time complexity.

Another thing I thought of which might be cool, but not mentioned by the question, is if the self.head customer is 
talking to a call representative and their call is deemed a different ranking as the customer and representative talk. 
In such a case, the customer put back into the stream of data inputted to the dictionary and put at the tail end of the 
newly designated, appropriate ranking. 

Solution 2:
A doubly linked list can be used instead of a singly linked list as the pointer to the previous node can be utilized 
effectively in this example. Also, doubly linked lists can be used to implement binary trees unlike singly linked lists.
I feel as thought this would be advantageous for something like a call center, or a telecommunications company in our 
case, to account for further features than proposed than in this question, such as calls dropped or elevation of
ranking. The customers are inputted with their ranking in the conventional .data parameter. A isEmpty() will be used
again here for the same purpose. This is constant time so we don't mind that in the grand scheme of things. Now, once
the doubly linked list is not empty, the next newly created Node will be appended and it's .data parameter (its 
ranking) will be compared against the previous node's data and if it's greater (higher priority as defined by the 
company) then its .prev parameter will point to the .prev.prev's node and in turn the .prev.prev's .next parameter will 
point to the the node at hand. And the node at hand's .next will point to the former .prev (the node that began the 
comparison. This comparison will happen until the node at hand meets attains self.head status, or reaches a node with
the same ranking priority as its data parameter. Additionally, this also extends to if the node at hand has a lower
rank priority it will stay at the tail end of the doubly linked list, pointing to None, until more new Nodes are
created for further comparison, etc. And similarly to solution 1, the customer/node at the self.head position is deleted
once dealt with and prompts the self.head.next Node to become the first node/self.head .
For time complexities:
Initially inserting the customers with their rankings into the doubly linked list will have at worst O(1) (this is the
same at best, too). Deleting the customer after they're dealt with also has a wost time complexity of O(1). However,
searching through the doubly linked list for a node to compare its ranking data will come with it a time complexity of
O(n) as it must traverse through the nodes one at a time (or 'n' at a time).


The same idea of reassigning customer ranking applies to this solution, but instead of the data reentering the input
stream seen in solution 1, it will be either elevated or demoted to a position closer or further away from the self.head
iff (if and only if) it's ranking is reassigned by the representative. This would cause O(n) in the worst case.

"""

###########################################################################
# # # # # # # # # # # # # # # Q U E S T I O N 5 # # # # # # # # # # # # # #
###########################################################################


def read_and_sort():
    from spacy.lang.en import stop_words, English

    nlp = English()

    # trout file
    with open('trout.txt') as trout_file:
        raw_text = trout_file.read().lower()
    # add stopwords to nlp's defined stop word vocabulary
    with open('stopwords.txt') as stopwords_file:
        lines = stopwords_file.read().split()
        # print(lines)
        for word in lines:
            term = nlp.vocab[word]
            term.is_stop = True

    tokenizer = nlp.tokenizer
    doc = nlp(raw_text)
    tokenized_words = [tok.text for tok in doc if tok.is_stop == False if tok.is_alpha]
    # tokenized_words

    from collections import defaultdict
    r = defaultdict(int)
    for token in tokenized_words:
        r[token] += 1

    values = r.values()
    # Return values of a dictionary
    total = sum(values)
    print("Token\tfreq\tprob")

    with open('trout.txt.probs', 'w') as file:
        file.write("Token\tfreq\tprob\n")
        for key, value in r.items():
            prob = value / total
            file.write(f"{key}\t{value}\t{prob}\n")

###########################################################################
# # # # # # # # # # # # # # # Q U E S T I O N 6 # # # # # # # # # # # # # #
###########################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

A = np.array([[22, 28, 52],
              [87, 12, 76],
              [44, 61, 81],
              [97, 4, 67],
              [52, 14, 24],
              [34, 82, 7]])

B = np.array([[88, 41, 22, 1, 14, 70, 7, 48, 64],
              [60, 10, 17, 34, 5, 57, 16, 98, 36]])

# Question 6.1

# Write your code here.
arr = np.max(np.power(A,2))
arr
# Question 6.2

# Write your code here.
summation = np.sum(A.argmin(axis=0))
summation
# Question 6.3

# Write your code here.
B = np.reshape(B, (6,3))
B
#np.concatenate(np.reshape(A,B),axis=1)
X = np.concatenate((A,B), axis=1)
np.mean(X, axis = 0)
# Question 6.4

# Write your code here.
C = np.concatenate((A,B))
C
Y = np.random.randint(1,99, size=(6,3))
Y
C = np.concatenate((C,Y))
C
#[random.uniform(low,high) for _ in range(size)]
#np.random.Generator.uniform(low=0.0, high=1.0, size=None)
# Question 6.5

# Write your code here.
import pandas as pd
df = pd.DataFrame(data=C, columns = ['X', 'Y', 'Z'])
df
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(data=df, x='X', y='Y', size = 'Z')
plt.title("A Very Informative Plot")
plt.show()