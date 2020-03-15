from os import remove, rename

def printInstructions(instruction):
    print(str(instruction))

def getUserScore(userName):
    try:
        fh = open('userScores.txt', 'r')
        # userScores file contain name, score per line

        for line in fh:
            #print(line)
            content = line.split(', ')
            if (content[0] == userName):
                print("Existing user (" + str(content[0]) + ") score = " + str(content[1]))
                fh.close()
                return content[1]
        fh.close()
        return -1
    except IOError:
        print('IOError')
    except Exception as e:
        print('unknown error' + str(e))


def updateUserScore(newUser, userName, score):
    print('hello from updateUserScore')
    if (newUser == 'True'):
        fp = open('userScores.txt', 'a')
        fp.write('\n' + userName + str(', ') + str(score))
        fp.close()
    elif (newUser == 'False'):
        # open a temporary file
        fp = open('userScores.tmp', 'w')
        fp_oldfile = open('userScores.txt', 'r')

        for line in fp_oldfile:
            content = line.split(', ')
            if (content[0] == userName):
                fp.write(userName + str(', ') + str(score) + '\n')
            else:
                fp.write(line)

        fp.close()
        fp_oldfile.close()
        # remove old file and rename new to same
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
    else:
        print('expected newUser to be True or False')


#printInstructions(getUserScore('Carol'))
#print(getUserScore1('Has'))
#updateUserScore('False', 'Ben', 190)
