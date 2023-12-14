#This implementation considers the List unordered
from node import Node
#defining the linked list itself
class UnorderedLinkedList:
    def __init__(self):
        self.head=None      #We initialise an empty linked list with the head element.

    def isEmpty(self):
        return self.head==None #In an empty node the head points to none
    
    def addItem(self,item):
        newNode=Node(item)
        newNode.setNext(self.head)
        self.head=newNode

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found
    
    def delete(self,item):
        '''
        Deleted a particular item from the linked list
        '''
        current=self.head
        found=False
        previous=None
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
        
    def __str__(self) -> str:
        current=self.head
        result=[]
        if current==None:
            return "Empty"
        while current!=None:
            for node in range(self.size()):
                result.append(str(current.data))
                current=current.getNext()
            return ' --> '.join(result)
            
    


