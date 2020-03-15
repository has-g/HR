# resource https://hackernoon.com/pythonic-way-of-doing-things-code-kq2b430vv

lst = [1, 4, "This message", 2.0, [3, 4, 5], {'a':'A', 'b':'B', 'c':'C'}, ('t1', 't2', 't3') ]

for element in lst:
    print(type(element))

elements = [type(element) for element in lst] # list comprehension
print(elements)
print(type(elements)) # elements type is of course a list

print("---------------")

custom_list = [[1,2,3,4,5],["Cat","Dog","Dog","Tiger","Lion","Goat"]]

# custom function to find square of a number
def square_of_number(x):
    return x*x

# using lambda functions to create a new list from exisitng list but with cube of each items in the list..
cube_of_number = lambda x:x*x*x
squares_of_list_items = lambda x:x*x
padded_with_2 = lambda x:x + 2

# using map function to apply a function to all elements of the list
new_list_of_squares = list(map(squares_of_list_items,custom_list[0]))
new_list_of_cubes = list(map(cube_of_number,custom_list[0]))
new_list_of_padded2 = list(map(padded_with_2, custom_list[0]))

print(new_list_of_squares)
print(new_list_of_cubes)
print(new_list_of_padded2)

# Using Enumerate to find the count of Each animal in custum_list
for i,x in enumerate(custom_list[1]):
    print('iterater is :', i ,'and value is ', x)