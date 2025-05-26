from linked_list import linked_list
from linked_list import node

list2 = linked_list()
list2.push_back(1)
print("back:", list2.back())
print("front:", list2.front())
list2.push_back(2)
print("back:", list2.back())
print("front:", list2.front())
list2.push_back(3)
print("back:", list2.back())
print("front:", list2.front())
print(list2.to_string())
print("contains 0:", list2.contains(0))
print("contains 4:", list2.contains(4))
print("contains 1:", list2.contains(1))
print("contains 2:", list2.contains(2))
print("contains 3:", list2.contains(3))
print("pop_back:", list2.pop_back())
print("pop_back:", list2.pop_back())
print("pop_back:", list2.pop_back())
try:
    print(list2.pop_back())
except IndexError:
    print("indexerror")

list2.push_back(1)
list2.push_back(2)
list2.push_back(3)
print("pop_front:", list2.pop_front())
print("pop_front:", list2.pop_front())
print("pop_front:", list2.pop_front())
try:
    print(list2.pop_front())
except IndexError:
    print("indexerror")

list2.push_front(1)
list2.push_front(2)
list2.push_front(3)
print("pop_back:", list2.pop_back())
print("pop_back:", list2.pop_back())
print("pop_back:", list2.pop_back())

list2.push_front(1)
list2.push_front(2)
list2.push_front(3)
print("pop_front:", list2.pop_front())
print("pop_front:", list2.pop_front())
print("pop_front:", list2.pop_front())

list2.push_back("apple")
list2.push_back("pear")
list2.push_back("grape")
list2.push_back("banana")
try:
    list2.insert_at(5, "orange")
except IndexError:
    print("indexerror")

list2.insert_at(2, "orange")
list2.remove_at(2)
print(list2.to_string())

print("contains apple:", list2.contains("apple"))

list2.remove("apple")
print(list2.to_string())

print("contains apple:", list2.contains("apple"))

list2.replace_at(2, "test")
print(list2.to_string())

list2.replace("test", "banana")
print(list2.to_string())

try:
    list2.remove("test")
except:
    print("valueerror")

list2.clear()
print(list2.to_string())
print(list2.get_size())