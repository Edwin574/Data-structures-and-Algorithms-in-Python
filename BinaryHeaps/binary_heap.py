
class BinaryHeap():
    def __init__(self):
        self.heap_list=[0]
        self.current_size=0
        
    def swap_up(self,i):
        while i//2>0:#as long as the given index if not the root/first element
            if not self.heap_list[i//2] <self.heap_list[i]:
                temp=self.heap_list[i//2]
                self.heap_list[i//2]=self.heap_list[i]
                self.heap_list[i]=temp
            i=i//2
        
    def insert(self,k):
        self.heap_list.append(k)
        self.current_size=self.current_size+1
        self.swap_up(self.current_size)
    
    def min_child(self,i):
        #we first check if the element at given index has a right child index that is within the list length
        if i*2+1>self.current_size:
            return i*2
        else:
            if self.heap_list[i*2]<self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1
            
    def swap_down(self,i):
        while (i*2)<=self.current_size:
            min_child=self.min_child(i)
            if self.heap_list[i]>self.heap_list[min_child]:
                temp=self.heap_list[i]
                self.heap_list[i]=self.heap_list[min_child]
                self.heap_list[min_child]=temp
            i=min_child
    
    def size(self):
        return self.current_size
    
    def delete_min(self):
        retun_value=self.heap_list[1]
        self.heap_list[1]=self.heap_list[self.current_size]
        self.current_size=self.current_size-1
        self.heap_list.pop()
        self.swap_down(1)
        return retun_value
    
    def is_empty(self):
        return self.current_size==1
    
    def build_heap(self,a_list):#**
        i=len(a_list)//2
        self.current_size=len(a_list)
        self.heap_list=[0]+a_list[:]
        while (i>0):
            self.swap_down(i)
            i=i-1
        
    def __str__(self) -> str:
        return f"{self.heap_list}"