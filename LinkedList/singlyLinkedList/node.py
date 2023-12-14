class Node():
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