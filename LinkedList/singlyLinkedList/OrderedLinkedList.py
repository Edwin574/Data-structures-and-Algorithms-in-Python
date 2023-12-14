
from node import Node

class OrderedLinkedList():
    def __init__(self):
        self.head=None

    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
            
    def is_empty(self):
        return self.head==None

    def addItem(self,item):
        current=self.head
        previous=None
        stop=False
        while current!=None and not stop:
            if current.getData()>item:
                stop=True
            else:
                previous==current
                current==current.getNext()
        new=Node(item)
        if previous==None:
            new.setNext(self.head)
            self.head=new
        else:
            new.setNext(current)
            previous.setNext(new)

    def searchItem(self,item):
        current=self.head
        found=False
        stop=False

        while current!=None and not found and not stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop=True
                else:
                    current=current.getNext()
        return found

    def deleteItem(self,item):
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