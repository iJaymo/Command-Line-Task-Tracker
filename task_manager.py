#Weclome messaage
print('Welcome to your Task Manager')
task_list = []

#Task Variables for strings
open_question = """                 
What would you like to do?
View Task. Type View
Add Task. Type Add
Complete Task. Type Complete
""")
add_task = "What task would you like to add?\n "
remove_task = "What task would you like to complete/remove?\n "
new_task = "Got it! Here is your new task list."
update_task = "Good job completing that! Here is an updated list for you."
invalid_response = "I'm sorry. I don't enderstand your response.\nPlease try again."

#need to add a task_list remove option as well.

task_response = input(open_question).lower()

while task_response == "view" or "add" or "complete":

  if task_response == "view"
    print(task_list)
  elif task_response == "add"
    task_list.append(input(add_task).lower()
    print(new_task)
    print(task_list)
  else:
    print(task_list)
    task_list.remove(input(remove_task).lower()
    print(update_task)
    print(task_list)
if task_response == "exit"
    # save data and close program
else:
  print(invalid_response)
  #repeat line 7
  
                    

  
      
      
    
  
  
        
