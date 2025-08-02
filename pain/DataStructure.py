class Node:
    def __init__(self, data: int):
        self.data  = data
        self.next  = None
        
class LinkyList:
    def __init__(self):
        self.head  = None
        
    
    def addE (self,n : int):
        newNode = Node(n)
        if self.head == None:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def addB (self, n : int):
        newNode = Node(n)
        if self.head == None:
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head = newNode
        
    def show(self):
        current = self.head
        while current:
            print(f"{current.data} ->",end=" ")
            current = current.next
        print("None")
