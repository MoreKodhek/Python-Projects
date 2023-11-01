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
        print("You walked for long and ran out of water and died")
        print("YOU LOSE!")
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks unsafe. Do you want to cross it or head back? (cross/back)")
    if answer == "cross":
        answer = input(
            "You cross the bride and meet a stranger, do you talk to them? (yes/no)")
    elif answer == "back":
        print("You go back to the main road, and found cannibals who cooked and ate you")
        print("YOU LOSE!")
else:
    print("Not a valid option, you LOSE!")
