
tasks = []


def menu():
    print("--------Welcome to the To Do List App-----")
    print('''These are the following options
          1.Add Tasks
          2.View Tasks
          3.Mark Tasks as Done
          4.Delete Tasks
          5.Exit App''')


def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append({'tasks': task, 'completed': False})
    print(f"task {task} added successfully")


def view_task(tasks):
    if tasks == []:
        print("no task yet!")
    else:
        print("-----Your Tasks-----\n")
        for i, item in enumerate(tasks):
            status = '✔️' if item['completed'] else ' '
            print(f"{i}.[ {status}  ] {item['tasks']}")


def mark_done(tasks):
    mrk = int(input("Enter the number of task u want to mark done: "))
    if 0 <= mrk < len(tasks):
        tasks[mrk]['completed'] = True
        view_task(tasks)
    else:
        print("invalid task no!")


def remove_task(tasks):
    view_task(tasks)
    remove = int(input("Enter the no of task u want to remove: "))
    if 0 <= remove < len(tasks):
        removed_task = tasks.pop(remove)
        print("task removed successfully!!")
    else:
        print("enter valid no.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            line = f"{task['tasks']}|{task['completed']}\n"
            file.write(line)
    print("Tasks saved successfully!")


def load_tasks():
    tasks=[]
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_text, completed = line.strip().split("|")
                tasks.append({"tasks": task_text, "completed": completed == "True"})
    except FileNotFoundError:
        pass  
    return tasks



def main():
    tasks = load_tasks()
    while True:
        menu()
        try:
            choice = int(input("Enter your choice from above: "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_task(tasks)
            elif choice == 3:
                mark_done(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                save_tasks(tasks)
                print("EXITING THE PROGRAM!!")
                break
        except ValueError:
            print("INVALID CHOICE")
    


main()

