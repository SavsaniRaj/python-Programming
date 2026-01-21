my_list = []

while True:
    print("\n------- List Operations Menu -------")
    print("1. Insert Element")
    print("2. Delete Element")
    print("3. Search Element")
    print("4. Display List")
    print("5. Sort List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert: "))
        my_list.append(element)
        print("Element Inserted.")

    elif choice == 2:
        element = int(input("Enter element to delete: "))
        if element in my_list:
            my_list.remove(element)
            print("Element Deleted.")
        else:
            print("Element not found in list.")

    elif choice == 3:
        element = int(input("Enter element to search: "))
        if element in my_list:
            print(f"Element found at index {my_list.index(element)}")
        else:
            print("Element not found.")

    elif choice == 4:
        print("Current List:", my_list)

    elif choice == 5:
        my_list.sort()
        print("List Sorted:", my_list)

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")
