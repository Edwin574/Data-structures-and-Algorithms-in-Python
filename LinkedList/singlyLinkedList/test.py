from UnorderedLinkedList import UnorderedLinkedList
mylist=UnorderedLinkedList()

mylist.addItem(31)
mylist.addItem(77)
mylist.addItem(17)
mylist.addItem(93)
mylist.addItem(26)
mylist.addItem(54)

print(mylist.search(93))

print(mylist)

mylist.delete(77)

print(mylist)
