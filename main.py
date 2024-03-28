#References
# https://realpython.com/run-python-scripts/ (python exec() built in fuction)


    # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    # Any code taken from other sources is referenced within my code solution.

    # Student ID: w1953232

    # Date: 17/4/2023 



# initializing variables
no_of_progress = 0
no_of_trailer = 0
no_of_exclude = 0
no_of_retriever = 0

# credit range
credit_list = [0, 20, 40, 60, 80, 100, 120]

# creating a list to enter user's progression data
progression_data = []

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


# user define function to check the total after getting user inputs
def process_outcome():
    while True:
        total = 0        
        pass_credits = user_credits("Please enter your credits at pass: ")
        defer_credits = user_credits("Please enter your credits at defer: ")
        fail_credits = user_credits("Please enter your credits at fail: ")

        #checking whether the total is correct (total = 120)
        total = pass_credits + defer_credits + fail_credits

        if total != 120:
            print("Total incorrect.\n")
            continue
            
        else:
            result(pass_credits, defer_credits, fail_credits)
            print(" ")
            break

    
# user define function to get progression of each student
def result(credits_passed, credits_defered, credits_failed):
    global no_of_progress, no_of_trailer, no_of_exclude, no_of_retriever # this can be used by both inside and outside of functions
    if credits_passed == 120:
        print("Progress")
        no_of_progress += 1 
        progression_data.append(["Progress - " ,credits_passed, credits_defered, credits_failed]) # adding data to the list

    elif credits_passed == 100:
        print("Progress (Module trailer)")
        no_of_trailer += 1
        progression_data.append(["Progress (Module trailer) - ",credits_passed, credits_defered, credits_failed])

    elif credits_failed >= 80:
        print("Exclude")
        no_of_exclude += 1
        progression_data.append(["Exclude - ",credits_passed, credits_defered, credits_failed])

    else:
        print("Do not progress - Module retriever")
        no_of_retriever += 1
        progression_data.append(["Do not progress - Module retriever - ",credits_passed, credits_defered, credits_failed])


# student version and staff version
run_program = True
while run_program:
    
    print("""      
                         STUDENT PROGRESSION     
                    ------------------------------

                        
                        Student version  - 1     
                        Staff version    - 2     
                        Dictionary       - 3     
                                               
     """)
     
    mode = input("Enter your option: ")
    print("")
    
    
    if mode == "1":
        process_outcome()
        break

    elif mode == "2":
        activate_code = True
        while activate_code:
            
            process_outcome() # calling the user define function

            while True:
                # asking whether user want to add more data (continue or not)
                choice = input(" \nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
                   
                if choice.lower() == "y":
                    print("")
                    break
                
                elif choice.lower() == "q":
                    # printng the histogram
                    print("_" * 55)
                    print("\nHistogram\n")
                            
                    print("Progress",no_of_progress,"   :",no_of_progress * "*" )
                    print("Trailer", no_of_trailer,"    :",no_of_trailer * "*")
                    print("Retriever", no_of_retriever,"  :",no_of_retriever * "*")
                    print("Excluded", no_of_exclude,"   :",no_of_exclude * "*")
                    
                    # calculating no of progression outcomes
                    total_outcomes = no_of_progress + no_of_trailer + no_of_exclude + no_of_retriever
                    print(" ")
                    print(total_outcomes, "outcomes in total.")
                    
                    print("_" * 55,"\n")
                    

                    # enter user's progression data to a list
                    print("Part 2:") 

                    for lists in progression_data:
                        
                      if lists[0] == 120:
                        print(f"{lists[0]}{lists[1]}, {lists[2]}, {lists[3]}")      
                        
                      elif lists[0] == 100:
                        print(f"{lists[0]}{lists[1]}, {lists[2]}, {lists[3]}")

                      elif lists[2] >= 80:
                        print(f"{lists[0]}{lists[1]}, {lists[2]}, {lists[3]}")

                      else:
                        print(f"{lists[0]}{lists[1]}, {lists[2]}, {lists[3]}")
                      
                    file = open("progression_output.txt", "w")
                    
                    for data_set in progression_data:
                        file.write(f"{data_set[0]} {data_set[1]}, {data_set[2]}, {data_set[3]} \n")
                    file.flush()
                    file.close()
                    
                    activate_code = False # exit from the outer loop
                    break
                

                else:
                    print("Invalid option")
                    continue

        #file.close() # closing the file which was in write mode

        print("\nPart 3:",end="")
        
        file = open("progression_output.txt", "r") 
        content = file.read() # reads the whole content of the file and stores in the variable content
        print(" ")
        print(content)

        file.close()  # clsoing the file which was in read mode
        break
    
    elif mode == "3":
      exec(open('w1953232_sd1_part4.py').read()) # if the user wants to go to the dictionary
      break
    
    else:
        print("Invalid option\n") 
        continue




        
