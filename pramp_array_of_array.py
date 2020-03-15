def array_of_array_products_2(arr):
    myNewList = []
    product = 1
    # go over array and make product
    for element in arr:
        product *= element

    print(str(product))
    # for each element divide product and get the number for each index
    for i in range(len(arr)):
        num = int(product/arr[i])

        # append to new list
        myNewList.append(num)

    print(myNewList)
    return myNewList



def array_of_array_products_3(arr):
    myNewList = []
    if len(arr) <= 1:
        return myNewList
    # step through index of each arr element
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if i != j:
                product *= arr[j]
        myNewList.append(product)
    return myNewList


def array_of_array_products_4(arr):
    myNewList = []
    myEvalList = []
    myEvalStr = ""
    n = len(arr)
    if n <= 1:
        return myNewList

    for i in range(n-1):
        myEvalList.append(arr[i])
        myEvalList.append('*')
    myEvalList.append(arr[n-1])
    print(myEvalList)

    myEvalStr = ''.join(str(myEvalList))
    print(myEvalStr)
    return []



def array_of_array_products(arr):
    n = len(arr)
    if n <= 1:
        return []

    print(arr)
    productArr = []
    product = 1
    for idx in range(n):
        productArr.append(product)
        product *= arr[idx]
    print(productArr)

    product = 1
    for j in range(n-1, -1, -1):
        productArr[j] *= product
        product *= arr[j]
        print("productArr[" + str(j) + "] = " + str(productArr[j]))
        print("product = " + str(product))

    return(productArr)

#print(array_of_array_products([8, 10, 2]))
print(array_of_array_products([2, 3, 4, 5]))
#print(array_of_array_products([1]))
#print(array_of_array_products([0]))
#print(array_of_array_products([2, 2]))
#print(array_of_array_products([]))
