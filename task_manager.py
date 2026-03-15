#Weclome messaage
print('Welcome to your Task Manager')
tasks_list = []

#need to add a task_list remove option as well.

task_response = input("""What would you like to do?
                         View Tasks. Type View
                         Add Task. Type Add
                         Complete Task. Type Complete
                         """).lower()

while task_response == "view" or "edit":

  if task_response == "view"
    print(task_list)
  elif task_response == "add"
    task_list,append(input("What task would you like to add?\n ")
    print("Got it! Here is your new task list.")
    print(task_list)
  else:
    print(task_list)
    task_list.remove(input("What task would you like to complete/remove?\n").lower()
    print("Good job completing that! Here is an updated list for you.")
    print(task_list)
if task_response == "exit"
    # save data and close program
else:
  print("I'm sorry. I don't enderstand your response.\nPlease try again.")
  #repeat line 7
  
                    

  
      
      
    
  
  
        
