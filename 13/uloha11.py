from random import randint
pravidla = """
• The game Nim starts out with seven sticks on the table.
• Each player takes turns picking up 1, 2 or 3 sticks and cannot pass.
• Whoever picks up the last stick loses (the other player wins).
• Input: The number of sticks the player is picking up
• Output:
• The number of sticks on the table
• Who won (the player or the computer)
• Other Information
• Whoever leaves 5 sticks for the other player can always win if they make the right followup move:
If the other player takes 1, you pick up 3
If the other player takes 2, you pick up 2
If the other player takes 3, you pick up 1
• Exact instructions:
1. Print the instructions
2. Set the number of stick at 7 and initialize other values
3. Find out if the user wants to go first or second
4. If the user goes second, have the computer take two sticks and the user goes
second, have the computer take two sticks.
5. As long as there is no winner, keep playing
5.1 While there is no winner
5.2 Find out how many sticks the user is taking
5.3 Make sure it’s a valid choice
5.3.1 Make sure the user picked 1, 2, or 3 sticks
5.3.2 Make sure that user didn’t take more sticks than are
on the table
5.4 Pick up the appropriate number of sticks.
5.5 Take the sticks off the table
5.6 See if there is a winner
"""
print(pravidla)

sticks = 7
turn = 1
print(f"Start of the game; {sticks} are on the table.")
if input("Do you want to go first? (y/n) ") == "n":
    sticks -= 2
    print(f"Computer took 2; There are {sticks} sticks left")
    turn = 1
flag = 0 # valid move = 0
while sticks > 0:
    flag = 0
    if turn ==1: #user
        inp = int(input("How many sticks do you want to take? "))
        if inp > 3 or sticks - inp < 0:
            flag = 1
        else:
            sticks -= inp
            print(f"You took {inp}; There are {sticks} sticks left")
    else: #computer
        inp = randint(1,3)
        if sticks - inp < 0:
            flag = 1
        else:
            sticks -= inp
            print(f"Computer took {inp}; There are {sticks} sticks left")

    if flag != 1:
        turn = 1 - turn

if turn == 0:
    print("You lost!")
else:
    print("You won!")