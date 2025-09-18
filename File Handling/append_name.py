with open("students.txt", "a") as f:
    while True:  
        name = input("Enter the Name: ")
        f.write(f"{name}\n")

        choice = input("Enter your choice (y to continue, e to exit): ").lower()
        if choice == "e":
            break