import random
from array_list import array_list

list = array_list()

list.push_back(1)
list.push_back(2)
list.push_back(3)
list.push_back(4)
list.push_back(5)
list.insert_at(1, 1.5)
list.insert_at(3, 2.5)

print(list.to_string())

list.clear()

print(list.to_string())

list.push_back(5)
list.push_back(3)
list.push_back(1)
list.push_back(4)
list.push_back(2)

print(list.to_string())

list.bubblesort()
print(list.to_string())

list.clear()

print(list.to_string())

list.push_back(2)
list.push_back(3)
list.push_back(4)
list.push_back(5)
list.push_back(1)

print(list.to_string())

list.quicksort()
print(list.to_string())

list.remove(2)
print(list.to_string())

print(list.to_string())

list.clear()

print(list.to_string())

for i in range(0, 25):
    list.push_back(random.randint(0, 100))

print(list.to_string())

list.mergesort()
print(list.to_string())