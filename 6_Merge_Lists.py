'''
Takes two sorted lists and merges them into a single sorted list. 
This function should take in two lists of whole numbers. 
The function should return a new sorted list which consists of the elements of the two arguments.
'''
def merge_lists(l1, l2):
    sorted_list = []

    # l1.extend(l2)
    # sorted_list = sorted(list(l1))

    sorted_list = sorted(list1 + list2)

    return sorted_list

list1 = [1, 2, 3, 5]
list2 = [4, 0, -10]
result = merge_lists(list1, list2)
print(result)