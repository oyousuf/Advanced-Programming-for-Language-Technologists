from sortarray import *


def quick_sort(sa):
	quick_sort_helper(sa,0,sa.getSize()-1)

	

def quick_sort_helper(sa, first, last): 
	if first>=last:	#it means that our list is already sorted-->base case
		return
	if first<last:	#recursive case  
		split_point = partition(sa, first, last)
		quick_sort_helper(sa, first, split_point-1) 
		quick_sort_helper(sa, split_point+1, last)	

def partition(sa, first, last): 
	pivot_value = first #pivot is the first item in the list
	left_mark = first + 1 #pivot is the first element, so left mark is the item after pivot
	right_mark = last

	done = False

	while not done:
		#increment left_mark until we locate a value that is greater than the pivot value
		while left_mark <= right_mark and sa.cmp(left_mark,pivot_value)<=0:
			left_mark = left_mark + 1 

		#decrement right_mark until we find a value that is less than the pivot value
		while left_mark <= right_mark and sa.cmp(right_mark,pivot_value) >= 0:
			right_mark = right_mark - 1

		if right_mark < left_mark:
			done = True	# exit while loop
		else: # swap the items that are out of place  and repeat the process 
			sa.swap(left_mark,right_mark)

	sa.swap(first,right_mark)	#the right mark is now the split point 
	return right_mark 





debug = False

sa = SortArray()
for size in range(30, 151, 20):
    print ("SIZE: ", size)

    for method in ["shuffle", "miniShuffle", "reverse"]:
        print ("METHOD: ", method)

        sa.reset(size, method)

        if debug:
            print ("before: ")
            sa.printList()
        
        quick_sort(sa)

        if debug:
            print ("after: ")
            sa.printList()

        sa.printInfo()
    
    print()







