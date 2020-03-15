def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    newList = my_list
    newList.extend(alices_list)
    newList.sort()
    print(newList)
    return newList

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

merge_lists(my_list, alices_list)
