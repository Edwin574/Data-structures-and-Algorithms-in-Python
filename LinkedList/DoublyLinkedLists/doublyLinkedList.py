
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
    
    def insert_between(self,data):
        new_node=Node(data)
        pred=self.head
        succ=pred.getNext()
        
        new_node.prev=pred
        new_node.next=succ
        
        succ.prev=new_node
        pred.next=new_node
        
        
        self.size+=1
        
      
    def searchItem(self):
        pass
    
    def deleteItem(self):
        pass
    
    def __str__(self) -> str:
        current=self.head.next
        if current==self.trailer:
            return "Empty"
        while current!=self.trailer:
            for _ in range(self.size):
                print(current.data)
                current=current.getNext()
    