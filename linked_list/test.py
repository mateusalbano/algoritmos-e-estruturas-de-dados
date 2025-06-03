from linked_list import linked_list
from linked_list import node

list = linked_list()
list.push_back(1)
print("back:", list.back())
print("front:", list.front())
list.push_back(2)
print("back:", list.back())
print("front:", list.front())
list.push_back(3)
print("back:", list.back())
print("front:", list.front())
print(list.to_string())
print("contains 0:", list.contains(0))
print("contains 4:", list.contains(4))
print("contains 1:", list.contains(1))
print("contains 2:", list.contains(2))
print("contains 3:", list.contains(3))
print("pop_back:", list.pop_back())
print("pop_back:", list.pop_back())
print("pop_back:", list.pop_back())
try:
    print(list.pop_back())
except IndexError:
    print("indexerror")

list.push_back(1)
list.push_back(2)
list.push_back(3)
print("pop_front:", list.pop_front())
print("pop_front:", list.pop_front())
print("pop_front:", list.pop_front())
try:
    print(list.pop_front())
except IndexError:
    print("indexerror")

list.push_front(1)
list.push_front(2)
list.push_front(3)
print("pop_back:", list.pop_back())
print("pop_back:", list.pop_back())
print("pop_back:", list.pop_back())

list.push_front(1)
list.push_front(2)
list.push_front(3)
print("pop_front:", list.pop_front())
print("pop_front:", list.pop_front())
print("pop_front:", list.pop_front())

list.push_back("apple")
list.push_back("pear")
list.push_back("grape")
list.push_back("banana")
try:
    list.insert_at(5, "orange")
except IndexError:
    print("indexerror")

list.insert_at(2, "orange")
list.remove_at(2)
print(list.to_string())

print("contains apple:", list.contains("apple"))

list.remove("apple")
print(list.to_string())

print("contains apple:", list.contains("apple"))

list.replace_at(2, "test")
print(list.to_string())

list.replace("test", "banana")
print(list.to_string())

try:
    list.remove("test")
except:
    print("valueerror")

list.clear()
print(list.to_string())
print(list.get_size())