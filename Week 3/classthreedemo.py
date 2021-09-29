# The amount of student groups.
num_student = int(input("How many students? "))
group_size = int(input("What is the group size? "))

num_groups = num_student / group_size
print(f"There are {num_groups} groups.")

full_groups = (num_student // group_size)
print(f"There are {full_groups} full groups.")

leftover_students = num_student % group_size
print(f"There are {leftover_students} students left over. ")
