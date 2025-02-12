print("Welcome to the Pattern Generator & Number Analyzer!")

print()

while True:
    print("Select an option:")
    print("1. Generate a pattern")                                            
    print("2. Analyze a range of numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
   
    print()

    if choice == 1:
        print("Choose a pattern type:")
        print("1. Right Angled Triangle")
        print("2. Pyramid")
        print("3. Left Angled Triangle")
        choice2 = int(input("Enter your choice: "))
        row = int(input("Enter number of rows for the pattern: "))
        print()
       
        if choice2 == 1:
            print("Pattern:")
            for i in range(1,row+1):
                for j in range(1,i+1):
                    print("*", end = " ")
                print()
           
        elif choice2 == 2:
            print("Pattern:")
            for i in range(1,row+1):
                for k in range(row,i,-1):
                    print(" ",end=" ")
                for j in range(1,i+1):
                    print("*", end = " ")
                for l in range(1,i):
                    print("*", end = " ")
                print()
           
        elif choice2 == 3:
            print("Pattern:")
            for i in range(1,row+1):
                for k in range(row,i,-1):
                    print(" ",end=" ")
                for j in range(1,i+1):
                    print("*", end = " ")
                print()
           
        else:
            print("Invalid choice...")
           
        print()
       
    elif choice == 2:
       
        start = int(input("Enter the start of the range:"))
        end = int(input("Enter the end of the range:"))
        sum = 0
       
        if end>start:
            for i in range(start,end+1):
                if i%2 == 0:
                    print("Number",i,"is Even")
                else:
                    print("Number",i,"is Odd")
                   
            for i in range(start,end+1):
                sum = sum + i
           
            print("Sum of all numbers from",start,"to",end,"is:",sum)
           
            print()
       
        else:
            for i in range(start,end-1,-1):
                if i%2 == 0:
                    print("Number",i,"is Even")
                else:
                    print("Number",i,"is Odd")
                   
            for i in range(start,end-1,-1):
                sum = sum + i
           
            print("Sum of all numbers from",start,"to",end,"is:",sum)
           
            print()
   
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break
   
    else:
        print("Invalid choice....")
