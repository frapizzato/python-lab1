
list = []
flag = 1

while(flag):
    print("Insert the number corresponding to the action you want to perform")
    print("1.   Insert a new task")
    print("2.   remove a task")
    print("3.   show all the task")
    print("4.   close the program")
    i=int(input("Your choice: "))

    if(i==1):
        s=input("Enter the new task: ")
        list.append(s)
    elif(i==2):
        r=input("Enter the task to remove: ")
        list.remove(r)
    elif(i==3):
        print("Here are all the tasks:")
        cnt = 1
        for task in list:
            print(cnt, task)
            cnt+=1
    elif(i==4):
        flag = 0
    else:
        print("Wrong command!")
