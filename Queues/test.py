from Queue import Queue

q=Queue()

q.enqueue(2)
q.enqueue('hello')
q.enqueue('dog')
q.enqueue('hell')
q.dequeue()
q.dequeue()
print(q)