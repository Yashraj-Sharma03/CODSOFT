print("<"*45,"To-do-list",">"*45)
def add():
    task = input("Enter the task to be completed: ")
    todo_list.append(task)
    print("Your task has been added in the To-do List successfully!")
    print("*"*90)
def update():
    pos = int(input("Enter the position of your task to be  updated: "))
    task = input("Enter new task that needs to be updated: ") 
    if (pos<1 or pos>len(todo_list)):
        print("Invalid Input.")
    else:
        todo_list[pos-1] = task
        print("Task updated successfully!")
        print("*"*90)
def done():
    pos = int(input("Enter the position of the task that has been completed: "))
    if (pos<1 or pos>len(todo_list)):
        print("Invalid Input.")
    else:
        todo_list[pos-1] = todo_list[pos-1]+": COMPLETED!"
        print("*"*90)
        
def todo():
    print("*"*90)
    for i in todo_list:
        print(i)
    print("*"*90)
while True:
    print("Choose an action to perform:\n1Create a to-do list.\n2.Add tasks to your list\n3.Update to-do list\n4.Mark as completed\n5.View the To-do List\n6.Exit")
    choice = int(input("Enter your choice: "))
    if (choice==1):
        todo_list = []
        com_list = []
        print("Your To-do list has been created successfully!")
        print("*"*90)
    elif(choice==2):
        add()
    elif(choice==3):
        update()
    elif(choice==4):
        done()
    elif(choice==5):
        todo()
    else:
        break
