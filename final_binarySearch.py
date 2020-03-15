import unittest

# search in arr, elemenent x, where limits are left and right
def binarySearch_recursive(arr, l, r, x):
    if r >= l:
        mid = l + (r-l)//2
        print(mid)

        # found at mid value
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            # left half
            return binarySearch_recursive(arr, l, mid-1, x)
        else:
            # right half
            return binarySearch_recursive(arr, mid+1, r, x)
    else:
        return -1

arr = [0, 3, 5, 7, 10]
r = len(arr) - 1
#print(binarySearch_recursive(arr, 0, r, 8))


def binarySearch_while(arr, l, r, x):
    while l <= r:
        mid = l + (r-l)//2

        if arr[mid] == x:
            # found it in middle
            return mid
        elif arr[mid] < x:
            # right side
            l = mid + 1
        elif arr[mid] > x:
            # item in left side
            r = mid -1

    return -1

arr = [0, 3, 5, 7, 10]
#arr = []
r = len(arr) - 1
#print(binarySearch_while(arr, 0, r, 8))

class Test(unittest.TestCase):
    def test_zero_list(self):
        expected = -1
        arr = [0, 3, 5, 7, 10]
        r = len(arr) - 1
        x = 8
        actual = binarySearch_while(arr, 0, r, x)
        self.assertEqual(actual, expected)
    def test_present(self):
        expected = 4
        arr = [0, 3, 5, 7, 10]
        r = len(arr) - 1
        x = 10
        actual = binarySearch_while(arr, 0, r, x)

#unittest.main(verbosity=1)


def binary_search_test(arr, l, r, x):
    while l <= r:
        mid = l + (r-l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            # x is to right side of array
            l = mid + 1
        else:
            # x is to tle left side of array
            r = mid - 1

    return -1

arr = [1, 2, 5, 6, 8, 10]
r = len(arr) - 1
x = 11
print(binary_search_test(arr, 2, r, x))

'''
def binarysearch(lst, el):
    if len(lst) == 0: return -1
    l = 0
    r = len(lst) - 1

    while l < r:
        m = l + (r - l)//2
        if lst[m] < el:
            l = m + 1
        elif lst[m] > el:
            r = m - 1
        elif lst[m] == el:
            return m
        else:
            print('invalid')

    return -1

print(binarysearch([1, 5, 6, 7, 9, 10, 13, 16, 18, 19], 8))
'''