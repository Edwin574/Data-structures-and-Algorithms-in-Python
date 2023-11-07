#This implementation considers the List unordered
#Defining the structure of a node in the Linked list.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def getData(self):
        return self.data

    def setData(self,new_data):
        self.data=new_data

    def getNext(self):
        return self.next
    
    def setNext(self,new_next):
        self.next=new_next

#defining the linked list itself
class SinglyList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None
    
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
                current.getNext()
        return found




