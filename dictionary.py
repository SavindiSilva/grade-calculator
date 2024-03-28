    # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    # Any code taken from other sources is referenced within my code solution.

    # Student ID: w1953232

    # Date: 17/4/2023 



# credit range
credit_list = [0, 20, 40, 60, 80, 100, 120]

# creating a dictionary to enter user's progression data
student_data = {}

# user define function for user input and validation
def user_credits(message):  
    while True:
        try:
            credit = int(input(message))

            if credit not in credit_list:
                print("Out of range.\n")
                continue

        except ValueError:
            print("Integer required.\n")
            continue

        break
    return credit


# user define function to get progression of each student
def result(credits_passed, credits_defered, credits_failed):
    if credits_passed == 120:
        print("Progress")
        
        student_data[student_id] = ["Progress",pass_credits, defer_credits, fail_credits] # adding data to the dictionary
        
    elif credits_passed == 100:
        print("Progress (Module trailer)")
        
        student_data[student_id] = ["Progress (Module trailer)",pass_credits, defer_credits, fail_credits]

    elif credits_failed >= 80:
        print("Exclude")
        
        student_data[student_id] = ["Exclude",pass_credits, defer_credits, fail_credits]
  
    else:
        print("Do not progress - Module retriever")
        
        student_data[student_id] = ["Do not progress - Module retriever",pass_credits, defer_credits, fail_credits]



print("\nPart 4: Dictionary (separate program)")
        
active = True
while active:
    
    try:
        student_id = input("\nEnter student ID: ")
        print("")
                
    except ValueError:
        print("Invalid student ID")
        
    # checks the validation of student id            
    if not student_id.startswith("w") or student_id[0].isupper() or len(student_id) != 8 or not student_id[1:].isdigit():
        print("Invalid student ID")
        continue
                  
    else:
        while True:
            total = 0
            pass_credits = user_credits("Enter your total PASS credits: ")
            defer_credits = user_credits("Enter your total DEFER credits: ")
            fail_credits = user_credits("Enter your total FAIL credits: ")
                     
            #checking whether the total is correct (total = 120)
            total = pass_credits + defer_credits + fail_credits
                                
            if total != 120:
                print("Total incorrect.\n")
                continue
                                    
            else:
                result(pass_credits, defer_credits, fail_credits)
                print(" ")
                break
               
    while True:
        # asking whether user want to add more data (continue or not)
        choice = input(" \nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
                           
        if choice.lower() == "y":
            break
        
        elif choice.lower() == "q":
            
            print(" ")
            for key, values in student_data.items(): # printing the dictionary
                print(f"{key}: {values[0]} - {values[1]}, {values[2]}, {values[3]}")
                  
            active = False # exit from the outer loop
            break
        
        else:
            print("Invalid option")
            continue

