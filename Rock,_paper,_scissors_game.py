# import libraries
import random

# print multiline instruction
# performstring concatenation of string
# Winning Rules as follows
print("Wining Rule of Rock, paper, scissors game\n"
      +"rock v/s paper => paper wins\n"
      +"paper v/s scissors => scissors wins\n"
      +"rock v/s scissors => rock wins")

# Run an infinite loop
while True:
    print("Enter your choice \nrock => 1\npaper => 2\nscissors => 3\n")
    # take the input from users
    User_choice = int(input("Your turn: "))
    # looping until user enter invalid input
    while 1> User_choice or 3< User_choice:
        User_choice = int(input(" Give the correct input !"))
    # initialize value of Users choice variable
    if User_choice == 1:
        choice = 'rock'
    elif User_choice ==2:
        choice = 'paper'
    elif User_choice ==3:
        choice = 'scissors'
    print("Now it's computer turn 😎")
    # Computer chooses randomly any number among 1 , 2 and 3. Using randint method of random module
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = 'rock'
    elif comp_choice ==2:
        comp_choice = 'paper'
    elif comp_choice ==3:
        comp_choice = 'scissors'
    print("Computer choice is =>", comp_choice) 
    print(choice, "v/s", comp_choice)
    # we need to check of a draw
    if choice == comp_choice:
        print("Match is draw")
    # Conditions for winning
    if choice == "rock" and comp_choice == "paper":
        print("Computer is win")
    elif choice == "paper" and comp_choice == "rock":
        print("you win")
    if choice == "paper" and comp_choice == "scissors":
        print("Computer is win")
    elif choice == "scissors" and comp_choice == "paper":
        print("You win")
    if choice == "scissors" and comp_choice == "rock":
        print("Computer is win")
    elif choice == "rock" and comp_choice == "scissors":
        print("You win")
    print("Do you want to play again (Y/N):")
    # user input to check, they want to play again or not 
    play_again = input().lower()
    if play_again == 'n':
        break

# after coming out of the while loop
# Print thanks for playing
print("Thank You for playing ")
