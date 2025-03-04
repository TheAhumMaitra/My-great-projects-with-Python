#Rock, paper, sizer game
import random
def game():
    #Intructions for user
    print("\n'R'- Rock, 'P'- Paper, 'S'- Sizer")
    #Inputs
    User_enter= input("Enter your input: ")
    Computer_input= random.randint(1,3)

    #Database
    Database= {
        "R": 1,
        "P": 2,
        "S": 3
    }

    #Results
    User_Result= Database[User_enter]

    #Result
    print(f"\n\nYour input {User_Result} and computer's input {Computer_input}")
    print("\n\nComputer inputs- '1'- Rock, '2'- Paper, '3'- Sizer")

    #Conditions or rules

    #Users result rules
    if (Computer_input==1 and User_enter=="P"):
        print("You win! Congrats!")
    elif (Computer_input==2 and User_enter=="S"):
        print("You win! Congrats!")
    elif (Computer_input==2 and User_enter=="R"):
        print("Computer win! You Lose!")
    elif (Computer_input==3 and User_enter=="P"):
        print("Computer win! You lose!")
    else:
        print("Same Values")
        game()


game()