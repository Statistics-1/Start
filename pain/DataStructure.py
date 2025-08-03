class Node:
    def __init__(self, data: int):
        self.data  = data
        self.next  = None
        
class LinkyList:
    def __init__(self):
        self.head  = None
        
    
    def addE (self, n):
        newNode = Node(n)
        if self.head == None:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
    
    def addB (self, n):
        newNode = Node(n)
        if self.head == None:
            self.head = newNode
            return
        
        newNode.next = self.head
        self.head = newNode
        return
    
    def addE(self, n : list):
        for i in n:
            newNode = Node(i)
            if self.head == None:
                self.head = newNode
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = newNode
                
    def addB (self, n : list):
        for i in n:
            newNode = Node(i)
            
            if self.head == None:
                self.head = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        return
        
    
    def removeE(self):
        current = self.head
        p  = None
        while current.next != None:
            p = current
            current = current.next
        p.next = None
        return current.data
    
    def removeB(self):
        current = self.head
        self.head = self.head.next
        return current.data
    
   
        
    
    def show(self):
        current = self.head
        while current:
            print(f"{current.data} ->",end=" ")
            current = current.next
        print("None")
