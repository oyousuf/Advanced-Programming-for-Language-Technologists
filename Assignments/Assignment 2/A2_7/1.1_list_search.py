from timeit import default_timer as timer


ordered_list = open('sortedWordList.txt', 'r')
unordered_list = open('toSearchFor.txt', 'r')

ordered_list_storing = [line.rstrip('\n') for line in ordered_list]
unordered_list_storing = [line.rstrip('\n') for line in unordered_list]


def list_seq_1(word_list, search_word):
    for index, words in enumerate(word_list):
        if search_word == words:
            return index
    return -1


def list_seq_2(word_list, search_word):
    for i in range(len(word_list)):
        if word_list[i] == search_word:
            return i
    return -1


def list_bi(word_list, search_word):
    first = 0
    last = len(word_list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if word_list[midpoint] == search_word:
            return midpoint
        else:
            if search_word < word_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return -1


def test():
    start = timer()
    for word in unordered_list_storing:
        list_seq_1(ordered_list_storing, word)
    end = timer()
    print(end - start)

    start = timer()
    for word in unordered_list_storing:
        list_seq_2(ordered_list_storing, word)
    end = timer()
    print(end - start)

    start = timer()
    for word in unordered_list_storing:
        list_bi(ordered_list_storing, word)
    end = timer()
    print(end - start)
    
