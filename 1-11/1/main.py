from queueM import QueueM

def menu():
    print("1. Insert a new node in the queue")
    print("2. Print the linked list")
    print("3. Delete a node from queue")
    print("4. Clear the queue")
    print("0. Exit")
    option = input()
    return option
    
def main():
    print("###Queue's test###")
    myQueue = QueueM()
    
    while True:
        choice = menu()
        
        if choice == '1':
            myQueue.push(input("Enter a item: "))
        elif choice == '2':
            print("-"*60)
            myQueue.print()
            print("-"*60)
        elif choice == '3':
            myQueue.pop()
        elif choice == '4':
            myQueue.clear()
        elif choice == '0':
            print("Closing...")
            break
        else:
            print("Invalid choice\n")
            
main()