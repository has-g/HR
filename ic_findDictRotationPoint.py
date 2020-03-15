def find_rotation_point(words):
    if len(words) == 0: return -1
    if len(words) == 1: return 0

    l = 0
    r = len(words) - 1
    mid = (r - l)//2

    count = 0
    while l <= r:
        if count == 20: return -3
        print("l=" + str(l) + ', r=' + str(r) + ', mid=' + str(mid))
        if words[mid] < words[r]:
            # rotation is on LHS
            r = mid
        elif words[mid] > words[r]:
            # rotation is on RHS
            l = mid
            if (r - mid) == 1:
                return r
        else:
            return -2
        mid = l + (r - l)//2
        count += 1

    return -1


myList = ['ptolemaic', 'retrograde', 'supplant',
     'undulate', 'xenoepist', 'asymptote',
     'babka', 'banoffee', 'engender',
     'karpatka', 'othellolagkage']

print(str(find_rotation_point(myList)))