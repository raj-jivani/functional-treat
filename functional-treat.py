all_data = []

while True:
    print("Welcome to the Data Analyzer and Tramsforemer programme")
    
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Thresold")
    print("5. Sort Data")
    print("6. Display dataset Statastic")
    print("7. Exit Programme")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            print("You have selected option 1")
            
            data = input("Enter data for 1D array (sepreted by space): ")
            
            a = list(data.split(" "))
            
            for i in a:
                b = int(i)
                all_data.append(b)
            
            print("data added successfully")
        
        case "2":
            print("You have selected option 2")
            
            print("Data Summary:")
            print("- Total Elements:", len(all_data))
            print("- Minimum value:", min(all_data))
            print("- Maximum value:", max(all_data))
            print("- Sum of all value:", sum(all_data))
            print("- Average value:",sum(all_data) / len(all_data))
            
        case "3":
            print("You have selected option 3")
            
            def factorial(num):
                if num == 0:
                    return 0
                return num * factorial(num - 1)
            
            number = int(input("Enter a number to calculate factorial: "))
            
            result = factorial(number)
            
            print(f"Factorial of {number} is: {result}")
            
        case "4":
            print("You have selected option 4")
            
            thresold_value = int(input("Enter a thresold value to filter out data above this value: "))
            
            filterd_data = list(filter(lambda x: x > thresold_value, all_data))
            print(f"Filterd Data (values > {thresold_value})")
            print(filterd_data)
        
        case "5":
            while True:
                print("You have selected option 5")
            
                print("Choose shorting option: ")
                print("- 1. Asscending")
                print("- 2. Descending")
                print("- 3. Exit")
            
                sort_choice = input("Enter your choice")
                
                match sort_choice:
                    case "1":
                        print("Sorted data in ascending order:")
                        all_data.sort()
                        print(all_data)
                        
                    case "2":
                        print("Sorted data in descending order:") 
                        all_data.sort(reverse=True)
                        print(all_data) 
                    
                    case "3":
                        print("Exiting the option")
                        break
                    
                    case _:
                        print("Invalid option") 
                        break
        case "6":
            print("You have slected option 6")
            
            def data_statistics(list):
                min_value = min(list)
                max_value = max(list)
                total_sum = sum(list)
                average_value = sum(list) / len(list)
                
                return min_value, max_value, total_sum, average_value
            
            result = data_statistics(all_data)
            
            print("Data Statistics:")
            print("- Minimum value:", result[0])
            print("- Maximum value:", result[1])
            print("- Sum of all value:", result[2])
            print("- Average value:", result[3]) 
            
        case "7":
            print("Thank you for using data analyzer and Tranformer Program. GoodBye!!!")
            break
        
        case _:
            print("Invalid option")
            break
    