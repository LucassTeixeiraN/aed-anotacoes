from node import Node

def menu():
    print("1. Fill in the list with 5 elements")
    print("2. Print list contents")
    print("3. Exit")
    
    option = input()
    return option


def main():
    print("###ONLY LINKED LIST###\n")
    myListHead = None
    
    while True:
        option = menu()
        
        if option == "1":  
            #Adds 5 nodes to the start of the linked list
            for count in range(1,6):
                myListHead = Node(count,myListHead)
        elif option == "2":
            #Prints the structure content
            if myListHead == None:
                print("List is empty")
            print()
            while myListHead != None:
                if myListHead.data == 1:
                    print(myListHead.data, "->||", end="")
                else:
                    print(myListHead.data,"->",end="") 
                myListHead = myListHead.next
        elif option == "3":
            print("Exiting...")
            break
        else:
            print("Invalid value")
main()