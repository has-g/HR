x = 9
print('sample output = ' + str(x))

y = 3.0
print(bool(y))
print(int(y))

name = 'Peter'
print(name.upper()) # returns uppercase
print(name.isalpha()) # boolean


make = 'Apple'
price = 1299
exchangerate = 1.2345343
message = 'The price of this %s laptop is %d at an exchange rate of >%.3f< usd to gbp' %(make, price, exchangerate)
print(message)
#pad the number output %9.3f gives 9 chars in all
print('PRINT INLINE: The price of this %s laptop is %d at an exchange rate of >%2d.3f< usd to gbp' %(make, price, exchangerate))

# use format to show index
print('FORMAT INLINE Price of {0:s} laptop is {1:d} at an exchange rate of {2:.3f} usd to gbp'.format(make, price, exchangerate))
