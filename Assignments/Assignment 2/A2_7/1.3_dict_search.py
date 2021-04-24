from timeit import default_timer as timer


ordered_list = open('sortedWordList.txt','r')
unordered_list = open('toSearchFor.txt','r')


dict_storing = [line.rstrip('\n') for line in ordered_list]
unordered_list_storing = [line.rstrip('\n') for line in unordered_list]


words_dict = {}
for index, word in enumerate(dict_storing):
    words_dict[word] = index


def dict_search(dictionary, search_word):
    return dictionary.get(search_word, -1)

def test():
    start = timer()
    for word in unordered_list_storing:
        dict_search(words_dict, word)
    end = timer()
    print(end - start)

