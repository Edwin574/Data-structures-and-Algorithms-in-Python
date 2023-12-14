class Node():
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
        
    def getData(self):
        return self.data
    
    def setData(self,new_data):
        self.data=new_data
        
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    