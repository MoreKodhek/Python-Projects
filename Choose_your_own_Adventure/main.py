name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across. Type 'Walk' to walk around and 'Swim' to swim through it: ")
    if answer == "swim":
        print("You swam across the river and were eaten by a crocodile.")
        print("YOU LOSE!")
    elif answer == "walk":
        print("You walked for long and ran out of water")
elif answer == "right":
    print()
else:
    print("Not a valid option, you LOSE!")
