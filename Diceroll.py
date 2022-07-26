'''import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":

    print(" Rolling the dices...")
    print("The values are....")
    print(random.random()).randint(min, max)
    print(random.random()).randint(min, max)

    roll_again = raw_input("Roll the dices again?")
'''
import random
min = 1
max = 6

numDices = 0
roll_again = "yes"
sum = 0

while roll_again == "yes" or roll_again == "y":
    numDices = int(input("how many dices "))
    for i in range(numDices):
        dicesArray = list(range(numDices))
        dicesArray[i] = random.randint(min, max)
        print(dicesArray[i])
        sum += dicesArray[i]
        print("sum ", sum)

    roll_again = input("Roll the dices again? ")
