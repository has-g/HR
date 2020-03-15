def ReverseWords(myList):

    originalListLength = len(myList)

    myString = "".join(myList)
    myWordList = myString.split()

    newList = []
    #print(myWordList)
    # range (start, stop[, step]) - reverse step
    for i in range( len(myWordList) - 1, -1, -1) :
        word = myWordList[i]
        for x in range(len(word)):
            #print('index = (' + str(i) + ', ' + str(x) + ')=' + word[x])
            newList.append(word[x])

        print('after each word>>' + str(newList))
        if (i != 0):
            newList.append(" ")

    if len(newList) == originalListLength:
        print('Success!' + '\n' )



ReverseWords([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ])
ReverseWords([ 'c', 'a', 'k', 'e',])
ReverseWords([ ])