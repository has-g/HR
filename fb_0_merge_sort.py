'''
https://stackabuse.com/sorting-algorithms-in-python/

sorting algorithm O(n logn) - space inefficient O(n)

compare with bubble O(n**2) - space efficient O(1)
'''

def merge_lists(left, right):
    sorted_list = []

    # We use the list lengths often, so its handy to make variables
    left_len = len(left)
    right_len = len(right)

    left_idx = 0
    right_idx = 0

    # go over full length of left + right list
    for _ in range(left_len + right_len):
        # if both the list indices are less than the length, i.e. still few more steppings to do
        if (left_idx < left_len) and (right_idx < right_len):
            if left[left_idx] <= right[right_idx]:
                sorted_list.append(left[left_idx])
                left_idx += 1
            else:
                sorted_list.append(right[right_idx])
                right_idx += 1
        elif left_idx == left_len:
            # left idx is exhausted, just copy the right ones
            sorted_list.append(right[right_idx])
            right_idx += 1
        elif right_idx == right_len:
            # right idx is exhausted, just copy the left ones
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            print('whoa?')

    return sorted_list

v = 1

def merge_sort(nums):
    # if single num, return it
    if len(nums) <= 1: return nums

    mid = len(nums) // 2

    # this is where the recursion occurs and we break the list down all the way
    # sort and merge each half
    left = merge_sort(nums[mid:])
    right = merge_sort(nums[:mid])

    global v
    v += 1
    print('v = ', str(v))

    return merge_lists(left, right)


print(merge_sort([8, 89, 45, 3, 2, 0, 77, 12, 45, -1, 66, 54]))
# the Alice cookie problem
#print(merge_lists([2, 4, 6, 8], [1, 7]))


