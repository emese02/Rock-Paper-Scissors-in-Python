from random import randint

def rock():
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__
    """)

def paper():
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

def scissors():
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def show_choice (choice):
    if choice == 1:
        rock()
    elif choice == 2:
        paper()
    else:
        scissors()

cond = True
while (cond is True):
    user_choice = int(input("1-Rock / 2-Paper / 3-Scissors: "))
    if user_choice not in [1,2,3]:
        print("The given data is not adequate")
    else:
        show_choice(user_choice)
        computer_choice = (randint(1, 3))
        show_choice(computer_choice)
        if user_choice == computer_choice:
            print("Draw")
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
            print("Congratulations!You won!")
        else:
            print("You lose. Better luck next time!")
