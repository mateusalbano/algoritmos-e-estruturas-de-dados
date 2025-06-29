import random
from array_list import array_list
from ordered_array_list import ordered_array_list

list = array_list()

list.push_back(1)
list.push_back(2)
list.push_back(3)
list.push_back(4)
list.push_back(5)
list.insert_at(1, 1.5)
list.insert_at(3, 2.5)
list.insert_at(7, 6)

print(list.to_string())

list.clear()

print(list.to_string())

for i in range(0, 25):
    list.push_back(random.randint(0, 100))

print(list.to_string())

list.bubblesort()
print ("\nbubblesort:")
print(list.to_string(), "\n")

list.clear()

for i in range(0, 25):
    list.push_back(random.randint(0, 100))

list.quicksort()
print ("\nquicksort:")
print(list.to_string(), "\n")

list.clear()

for i in range(0, 25):
    list.push_back(random.randint(0, 100))

list.mergesort()
print ("\nmergesort:")
print(list.to_string())

list = ordered_array_list()
for i in range(10):
    list.insert(random.randint(0, 10))

print("\nordered list:")
print(list.to_string())
print("\none at position: ", list.search(1))
