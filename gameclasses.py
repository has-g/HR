from random import randint

class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions
        #print("__init__ method for base class Game invoked")

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("Minimum number of questions = 1\nHence number of questions set to 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("Maximum number of questions = 10\nHence number of questions set to 10")
        else:
            self._noOfQuestions = value
            print("Setter: num of questions set to = " + str(self.noOfQuestions))


class BinaryGame(Game):
    def generateQuestions(self):
        # import randint

        # declare local variable called score
        score = 0

        # use a loop to generate questions and evaluate answers
        for index in range(self.noOfQuestions):
            base10number = randint(1, 100)
            userPrompt = str(index+1) + ") What is the binary equivalent of this number = " + int(base10number)
            userResult = input(userPrompt)
            while true:
                try:
                    # cast users answer to an int and evaluate answer
                    answer = int(userResult, base=2)
                    # update user score based on this
                    if (answer == base10number):
                        print("correct!")
                        score += 1
                    else:
                        print("Incorrect!, correct answer is {:b}.".format(base10number))
                    # break out using  a break statement
                    break

                except:
                    # print error if casting fails
                    print("Error occurred in casting user input ")
                    # prompt user to key in answer again
                    userResult = input(userPrompt)

        # return score value
        return score


class MathGame(Game):
    def generateQuestions(self):
        # import randint
        # declare local variables called score, numberList, symbolList, operatorDict
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1:"+", 2:"-", 3:"*", 4:"**"}

        # use a loop to generate questions and evaluate answers
        for index in range(self.noOfQuestions):
            # build the list with single digit number generated with randint
            for i in range(len(numberList)):
                numberList[i] = randint(1, 9)

            # generate a symbol randomly to begin to create a math problem
            for x in range(len(symbolList)):
                symbolList[x] = operatorDict[randint(1,4)]
                if x > 0:
                    if ((symbolList[x] == "**") & (symbolList[x-1] == "**")):
                        symbolList[x] = operatorDict[randint(1,3)]

            # add symbol and numbers to the first number
            questionString = str(numberList[0])
            for y in range(len(symbolList)):
                questionString = questionString + symbolList[y] + str(numberList[y])

            expectedResult = eval(questionString)
            print("Expected result ...ssshhh! = " + str(expectedResult))
            questionStringReadable = questionString.replace("**", "^")

            userPrompt = str(index + 1) + ") What is the answer for " + questionStringReadable + '\n'
            userResult = input(userPrompt)

            while True:
                try:
                    # cast users answer to an int and compare with expected result
                    answer = int(userResult)
                    print(">>> input (int) =" + str(answer))

                    # update user score based on this
                    if (answer == expectedResult):
                        print("correct answer")
                        score += 1
                    else:
                        print("Incorrect!, " + str(answer) + ", Correct answer is " + str(expectedResult))

                    # break out using  a break statement
                    break

                except:
                    # print error if casting fails
                    print("Error occurred in casting user input ")
                    # prompt user to key in answer again
                    userResult = input(userPrompt)

        # return score value
        return score



#MathGame(3)
#BinaryGame.generateQuestions()
