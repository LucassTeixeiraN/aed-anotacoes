from linkedUnorderedList import UnorderedLinkedList

def menu():
    print("1. Insert a new node at the beggining")
    print("2. append a new node at the end")
    print("3. insert a new node after the given prevnode")
    print("4. print the linked list")
    print("5. seach a node")
    print("6. delete a node at the beggining")
    print("7. delete a node at the end")
    print("8. delete a node given a key")
    print("9. clear all list")
    print("0. exit")
    
    option = input()
    return option


def main():
    print("###ONLY LINKED LIST###\n")
    myListHead = None
    
    while True:
        option = menu()
        myList = UnorderedLinkedList()
        
        if option == "1":  
            myList.push(input("enter a item:  "))

        elif option == "2":
            myList.append(input("enter a item:  "))
        elif option == "3":
            myList.insertAfter(myList.searchNode(input("Enter a previous item:   ")))
        elif option == "4":
            myList.printList()
        elif option == "5":
            if myList.searchNode(input("Enter a item: ")):
                print("item found")
            else:
                print("item not found")
        elif option == "6":
            myList.pop()
        elif option == "7":
            myList.popEnd()
        elif option == "8":
            myList.deleteNode(input("Enter a item: "))
        elif option == "9":
            myList.clear()
        elif option == "0":
            print("Quiting...")
            break
        else:
            print("Invalid value")
main()