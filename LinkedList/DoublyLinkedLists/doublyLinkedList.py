
from node import Node

class DoublyLinkedList():
    def __init__(self):
        self.head=Node(None,None,None)
        self.trailer=Node(None,None,None)
        
        self.head.next=self.trailer
        self.trailer.prev=self.head
        
        self.size=0
        
    def size(self):
        return self.size
    
    def addItem(self,data):
        #when we start
        new_node=Node(data=data)
        return new_node
        
    
    def searchItem(self):
        pass
    
    def deleteItem(self):
        pass
    
    def __str__(self) -> str:
        current=self.head
        if current.next==self.trailer:
            return "Empty"
        while current.next!=self.trailer:
            for node in range(self.size):
                print(current.data)
                current=current.getNext()
    