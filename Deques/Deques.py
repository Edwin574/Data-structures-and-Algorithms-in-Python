'''
Implementing a Deque where index 0 is the "front" while the last index is the "rear"
'''

class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]
    
    def add_front(self,item):
        self.items.insert(0,item)
        
    def add_rear(self,item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)
    
    def remove_rear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def __str__(self) -> str:
        return (f"{self.items}")

