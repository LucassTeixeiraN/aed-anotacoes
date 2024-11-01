from node import Node

class QueueM:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def push(self, newData):
        newNode = Node(newData)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    
    def print(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            temp = self.head
            while temp:
                print(f"{temp.data} ")
                temp = temp.next
            
    def pop(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            penult = self.head
            last = self.head
            while last.next:
                penult = last
                last = last.next
            penult.next = None
            self.tail = penult
            
    def clear(self):
        if self.isEmpty():
            print("Empty queue")
        else:
            self.head = None