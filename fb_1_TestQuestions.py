'''
In order to win the prize for most cookies sold, my friend Alice and
I are going to merge our Girl Scout Cookies orders and enter as one unit.
Each order is represented by an "order id" (an integer).
We have our lists of orders sorted numerically already, in lists.
Write a function to merge our lists of orders into one sorted list.
For example:
 my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists(my_list, alices_list)
Solution:
 def merge_sorted_lists(arr1, arr2):
    return sorted(arr1 + arr2)
'''

def merge_sorted_lists(arr1, arr2):
    sorted_arr = []
    idx1 = 0
    idx2 = 0

    if len(arr1) == 0: return arr2
    if len(arr2) == 0: return arr1
    count = 0

    while count < len(arr2) + len(arr1):
        print('count = ' + str(count) + ', idx1 = ' + str(idx1) + ', idx2 = ' + str(idx2) + ', sorted_arr = ' + str(sorted_arr))
        if idx2 >= len(arr2):
            # idx2 is exhausted
            sorted_arr.append(arr1[idx1])
            idx1 += 1
        elif idx1 >= len(arr1):
            # idx1 is exhausted
            sorted_arr.append(arr2[idx2])
            idx2 += 1
        elif arr2[idx2] < arr1[idx1]:
            sorted_arr.append(arr2[idx2])
            idx2 += 1
        else:
            sorted_arr.append(arr1[idx1])
            idx1 += 1
        count += 1
    return sorted_arr


print(merge_sorted_lists([2, 4, 6, 8], [1, 7]))
#print(merge_sorted_lists([], [1, 7]))
#print(merge_sorted_lists([2, 4, 6], [1, 3, 7]))

