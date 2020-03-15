print("what's your name?")
myname = input()
print("and what about your age.... How old are you?")
myage = input()
print("your name is = " + myname + " and you are " + myage + " years old")
print("your name is {0:s} and you are {1:s} years old".format(myname, myage))
print("your name is %s and you are %s years old" %(myname, myage))


# raw output
print('this is a \t output with a newline \n newline')
print(r'this is a \t output and no newline \n')