from Deques import Deque

d=Deque()
print(d.is_empty())
print(d.add_rear(4))
d.add_rear('dog')
d.add_front('cat')
d.add_front('True')
print(d.size())

d.add_rear(8.4)
print(d.remove_rear())
d.remove_front()
print(d)