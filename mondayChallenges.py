# create two lists of items ✔️
# print the two lists as a table ✔️
# user input a item to a prompt and only that name from the table prints ✔️
# add a new item and sort the lists ✔️
# create a text document with the lists (up to you 2 files or 1 file) ✔️ 
# read from the lists ✔️
# edit lines and write to lists 

import csv

# table
def table():
    i = 0
    print("-" * len(f"| {list1[i]} | {list2[i]} |"))
    for _ in range(len(list1)):
        print(f"| {list1[i]} | {list2[i]} |")
        print("-" * len(f"| {list1[i]} | {list2[i]} |"))
        i += 1

# list with 2 things
list1 = ["pizza", "pasta", "chips"]
list2 = ["$10", "$5", "$2"]
paired = [list1, list2]

# add new item to list
# new_item1 = input("New item 1: ")
# list1.append(new_item1)
# new_item2 = input("New item 2: ")
# list2.append(new_item2)

table()

# item search
# item = input("find an item ")
# # enumerate is black magic (it gives the spot and the item)
# for i, list_item in enumerate(list1):
#     if item == list_item:
#         print(list2[i])
# for i, list_item in enumerate(list2):
#     if item == list_item:
#         print(list1[i])

# new item and sort
while True:
    try:
        new_item1 = input("Column 1: ")
        list1.append(new_item1)
        # list1.sort()
        new_item2 = input("Column 2: ")
        list2.append(new_item2)
        # list2.sort()
    except EOFError:
        break

table()

# save as file
file_name = input("file nmae: ")
with open(file_name, "w") as file:
    for i, list_item in enumerate(list1):
        file.write(f"{list1[i]}, {list2[i]} \n")

# read file (its the one you just saved fo now)
with open(file_name) as file:
    for line in file:
        col1, col2 = line.split(", ")
        print(f"the {col1} is {col2}".rstrip())