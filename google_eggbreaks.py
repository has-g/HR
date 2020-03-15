def EggBreaks(x):
    l = 0
    h = 0

    lowestgoodfloor = l
    highestgoodfloor = r

    while l < r:
        m = l + (h - l)// 2

        if x == m:
            highestgoodfloor = m
            lowestgoodfloor = l
            break
        if x < m:
            lowestgoodfloor = l
            break
        if x > m:
            l = m + 1
            lowestgoodfloor = m


n2 + n - 200 = 0
a = 1
b = 1
c = -200

sqrt(-1 +/- 800)/2 = 14 floors


14 - 14
13 - 27
12 - 39
11 - 50
10 - 60
9  - 69
8  - 77
7  - 84
6  - 90
5  - 95
4  - 99
