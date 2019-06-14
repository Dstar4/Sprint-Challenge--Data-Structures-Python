import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# loops through names 2 for every name in name_1
# loops through 10,000 names 10,000 times

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime: 6.5317909717559814 seconds

# loops through names_2 and checks if it is in names_1_set
# sets have no index or slicing and can hold any type of data
# membership tests are faster in a set because they use a hash table
# so a set will reduce one of our for loops to a O(1) operation

names_1_set = set(names_1)
for name in names_2:
    if name in names_1_set:
        duplicates.append(name)

# runtime: 0.003815174102783203 seconds

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
