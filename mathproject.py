from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, MathGame, BinaryGame

print("========")
try:
    # declare variables
    mathInstructions = "In this game, you will be given a simple arithmetic question. Each correct answer gives you one point. Nothing deducted for wrong answers. Best of luck!"
    binaryInstructions = "In this game, you will be given a number in base10." \
                         "Your task is to convert this number to base2 (e.g. 0b1010)." \
                         "Each correct answer gives you one point.\nNothing deducted for wrong answers." \
                         "Best of luck!"


    # instantiate two objects mg and bg
    mg = MathGame()
    bg = BinaryGame()

    userName = input("Enter your username: ")

    score = int(getUserScore(userName))
    #print(">>" + userName +"<< score >>" + str(score) + "<<")
    if (score == -1):
        newUser = "True"
        score = 0
    else:
        newUser = "False"

    #print("Is new user? " + str(newUser))
    # use a while loop to run the program until the user chooses to exit
    userChoice = 0

    while (userChoice != '-1'):
        # prompt user to select Math game or Binary game
        game = input("Math Game (1) or Binary Game (2), Exit (-1)?\n")
        # prompt user for number of questions per game
        numPrompt = input("How many questions do you want per game (1 - 10)?\n")
        while True:
            try:
                # cast to an int
                numInt = int(numPrompt)
                break
            except:
                print("Invalid entry " + str(numPrompt))
                numPrompt = input("How many questions do you want per game (1 - 10)?")

        # display relevant questions based on user's selection and update user's score
        if (game == '1'):
            mg.noOfQuestions = numInt
            #print(mg.noOfQuestions)
            printInstructions(mathInstructions)
            score += mg.generateQuestions()
        elif (game == '2'):
            bg.noOfQuestions = numInt
            printInstructions(binaryInstructions)
            score += bg.generateQuestions()
        else:
            print("! Invalid game code " + str(game))

        # display updated score to user
        print("New Score (" + userName + ") = " + str(score))

        # prompt user to enter a choice and use it to update userChoice
        prompt = input("Press Enter to continue of enter -1 to exit")
        if (prompt == '-1'):
            userChoice = -1

    # update the user's score after he exits
    updateUserScore(newUser, userName, str(score))

except Exception as e:
    print("Unknown Error, program will exit...error = " + str(e))