from timeit import default_timer as timer
import collections


ordered_list = open('sortedWordList.txt','r')
unordered_list = open('toSearchFor.txt','r')


ordered_deque_storing = collections.deque([line.rstrip('\n') for line in ordered_list])
unordered_deque_storing = collections.deque([line.rstrip('\n') for line in unordered_list])


def deque_seq_1(word_deque, search_word):
    for index, word in enumerate(word_deque):
        if search_word == word:
            return index
    return -1


def deque_seq_2(word_deque, search_word):
    for i in range(len(word_deque)):
        if word_deque[i] == search_word:
            return i
    return -1


def deque_bi(word_deque, search_word):
    first = 0
    last = len(word_deque) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if word_deque[midpoint] == search_word:
            return midpoint
        else:
            if search_word < word_deque[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return -1


def test():
    start = timer()
    for word in unordered_deque_storing:
        deque_seq_1(ordered_deque_storing, word)
    end = timer()
    print(end - start)

    start = timer()
    for word in unordered_deque_storing:
        deque_seq_2(ordered_deque_storing, word)
    end = timer()
    print(end - start)

    start = timer()
    for word in unordered_deque_storing:
        deque_bi(ordered_deque_storing, word)
    end = timer()
    print(end - start)
