from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = "Stewart"
print_time("printed first name")

for x in range (0,10):
    print(x)
print("completed for loop")
