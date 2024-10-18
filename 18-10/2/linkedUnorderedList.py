from node import Node

class UnorderedLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    
    def push(self, newData):
        newNode = Node(newData)
        
        if self.isEmpty():
            self.head = newNode    
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def append(self, newData):
        newNode = Node(newData)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def insertAfter(self, prevNode, newData):
        if prevNode is None:
            print("The given previous node must inLinkedList")
            return

        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        
    def printList(self):
        if self.isEmpty():
            print("Empty list")

        else:
            temp = self.head
            while temp:
                print(temp.data,"",end="")
                temp = temp.next
                
    def searchNode(self, data):
        if self.isEmpty():
            print("Empty List")
        else:
            temp = self.head
            while temp:
                if  temp.data == data:
                    return temp
                temp = temp.next
            return None
        
    def pop(self):
        
        if self.isEmpty():
            print("empty list")
        else:
            self.head = self.head.next
    
    
    def popEnd(self):
        
        if self.isEmpty():
            print("empty list")
        else:
            penult = self.head
            last = self.head
            while last.next:
                penult = last
                last = last.next
            penult.next = None
            
    def deleteNode(self, key):
        
        if self.isEmpty():
            print("empty list")
        else:
            temp = self.head
            
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            while temp is not None:
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next
                if temp == None:
                    return
                prev.next = temp.next
                temp = None
    def clear(self):
        
        if self.isEmpty():
            print("empty list")
        else:
            self.head = None       