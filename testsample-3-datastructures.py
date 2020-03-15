userage = [44, 40, 9, 4]
print('family age = ' + str(userage)) # returns me full list as is
print('family age = ' + str(userage[0:])) # returns me range starting at 0 index until end since not

userage2 = userage.count(5)
print('list userage2 = ' + str(userage2))

userage.append(99)

userage3 = userage
print(userage3)

del userage3[0]
print(userage3)

print(userage[-1:]) # note userage[-1:] returns a list

usernameandage = dict() # empty dictionary declaration
usernameandage = {"has":44, 'eriko':42, 'mia':9, 'sami':4} #type1 dictionary declaration
#usernameandage = dict('has'=44, eriko=42, mia=9, sami=4)     #type2 dictionary declaration
print(usernameandage)
print('has is going to be = ' + str(usernameandage['has']))

usernameandage['dog'] = 'not yet'
print(usernameandage)

print('what dog? = ' + usernameandage['dog'])

del usernameandage['dog'] # removed dog
print(usernameandage)
