###----------Challenge 1----------#####
list1 = []
list2 = []
name = input("User 1 please enter a name to add to the list: ")
while name.lower() != "q":
    list1.append(name)
    name = input("Enter a name to add to the list (or 'q' to quit): ")
name = input("User 2 please enter a name to add to the list: ")
while name.lower() != "q":
    list2.append(name)
    name = input("Enter a name to add to the list (or 'q' to quit): ")
print("First list: \n ", list2)
print("Second list: \n ", list1)
common_friends = set(list1) & set(list2)
print("Common names in both lists: ", common_friends)