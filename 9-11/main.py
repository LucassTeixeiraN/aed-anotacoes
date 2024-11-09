from binarySearchTree import BinarySearchTree

def menu():
    print("1. Insert a number in the tree")
    print("2. Search a tree node")
    print("3. Verify the entire tree in order")
    print("4. Verify the entire tree in pre-order")
    print("5. Verify the entire tree in post-order")
    print("6. Finde the smallest element in the tree")
    print("7. Finde the biggest element in the tree")
    print("8. Find the tree's height")
    print("9. Count how many nodes there are in the tree")
    print("10. Delete a tree node")
    print("11. Print the tree")
    print("0. Exit")

    return input("Choose an option: ")

def main():
    tree = BinarySearchTree()
    
    while True:
        option = menu()
        
        if option == "1":
            tree.insert(tree.root, input("Enter an element: "))
        elif option == "2":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                value = input("Enter a value: ")
                print("Element found!" if tree.search(tree.root, value) else "Element not found!")
        elif option == "3":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print("In order: ", end="") 
                tree.printInOrder(tree.root)
        elif option == "4":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print("Pre order: ", end="") 
                tree.printPreOrder(tree.root)
        elif option == "5":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print("Post order: ", end="") 
                tree.printPostOrder(tree.root)
                
        elif option == "6":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print(tree.minNode(tree.root))
        elif option == "7":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print(tree.maxNode(tree.root))
        elif option == "8":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print(tree.heightTree(tree.root))
        elif option == '9':
            if tree.isEmpty():
                print("Tree empty!")
            else:
                print(tree.countNodes(tree.root))
        elif option == '10':
            if tree.isEmpty():
                print("Tree empty!")
            else:
                tree.delete(tree.root, input("Enter a value: "))
        elif option == "11":
            if tree.isEmpty():
                print("Tree empty!")
            else:
                tree.printTree(tree.root, 0)
        elif option == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose a valid option.")