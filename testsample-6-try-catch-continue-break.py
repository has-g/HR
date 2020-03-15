print('\n------------ try catch example 2 -------------')
result = 0
try:
    userinput1 = int(input('Enter an integer int1= '))
    userinput2 = int(input('Enter an integer again int2= '))
    result = userinput1/userinput2

    filename = open('missingfile.txt', 'r')
except RuntimeError as e:
    print('Exception RuntimeError %s', {e})

except ValueError as e:
    print('Exception ValueError %s' %(e))
    #print('Exception ValueError ', e)

except ZeroDivisionError as e:
    print('Exception ZeroDivisionError', e)

except IOError as e:
    print('IOError ', e)

#except Warning as e:
#    print('Warning ', e)

except Exception as e:
    print('unknown error as e', e)

print('result = ' + str(result))

"""
print('\n------------ try catch example 1 -------------')
n = 0
j = 0
try:
     j = 12/n
except ZeroDivisionError:
    print('Exception with error type ZeroDivisionError j=' + str(j))
except Exception as e:
    print('unknown error')

print('\n------------ break example -------------')
j=0
for i in range(0,5):
    j += 2
    print('i = ' + str(i) + ' and j = ' + str(j))
    if j == 6:
        print('how did i get here? Bingo that\'s because j = 6')
        break

print('\n------------ continue example -------------')
j=0
for i in range(0,5):
    j += 2
    if j == 6:
        print('>> exclusively executed line >> j = ' + str(j))
        continue
    print('i = ' + str(i))

"""