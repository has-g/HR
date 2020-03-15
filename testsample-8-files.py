f = open('/Users/eshimpo/PycharmProjects/hr/iofiles/inputfile.txt', 'r')

'''
try:
    firstline = f.readline()
    print(firstline, end='')
except Exception as e:
    print(e)
'''

try:
    line = f.readline()
    while (line != ""):
        print(line, end = '')
        line = f.readline()
except Exception as e:
    print(e)

f.close()

print('\n======== copying over binary file =========')
binfile = open('/Users/eshimpo/PycharmProjects/hr/iofiles/IMG_2189.jpg', 'br')
newfile = open('/Users/eshimpo/PycharmProjects/hr/iofiles/IMG_new.jpg', 'ba')

msg = binfile.read()
newfile.write(msg)

newfile.close()
binfile.close()