

#using the end of the list as the top of the stack
class Stack1:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

#We can also implement the stack using the first item in the list as the top of the stack
#In this case the push and pop methods will have to change
class Stack2:
    def __init__(self):
        self.items=[]
       
    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    def __repr__(self):
        return f'['+self.items+']'