####----------Challenge 3----------#####
import random
Bag = [random.randint(0, 100) for _ in range(5)]
while True:
    print("Bag: ", Bag)
    action = int(input("Enter 1 to add a number, 2 to remove a number, or 0 to exit: "))
    if action == 1:
        AddNumber = int(input("Enter the number you want to add: "))
        Bag.append(AddNumber)
    elif action == 2:
        RemoveNumber = int(input("Enter the number you want to remove: "))
        if RemoveNumber in Bag:
            Bag.remove(RemoveNumber)
        else:
            print("Number not in Bag.")
    elif action == 0:
        break
    else:
        print("Invalid input. Please enter 1, 2, or 0.")