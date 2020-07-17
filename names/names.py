import time
from binary_search_tree import BSTNode
from singly_linked_list import Node
from singly_linked_list import LinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#binary search tree
binary_1 = BSTNode('jim')
for i in names_1:
    binary_1.insert(i)

for i in names_2:
    if binary_1.contains(i):
        duplicates.append(i)

#linked list
# singly_1 = LinkedList()
# for i in names_1:
#     singly_1.add_to_tail(i)

# for i in names_2:
#     if singly_1.contains(i):
#         duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
