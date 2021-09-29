runners = []
times = []

runners.append("Jimmy Bolt")
runners.append("Stewart")
runners.append("Spongebob")
runners.append("Patrick")

times.append(17)
times.append(19)
times.append(65)
times.append(120)

for i in range(len(runners)):
    print(f"{i+1}. {runners[i]} - {times[i]}")
    # cur_runner = runners[i]
    # cur_times = times[i]

    # print(f"{cur_runner} - {cur_time}")

# runners.pop(1) and times.pop(1)
number_to_replace = int(input("What number do you want to replace? "))
index_to_replace = number_to_replace - 1

name = input("What is the new name? ")
time = int(input("What is the new time? "))

# This will replace the current spot 
runners[index_to_replace] = name
times[index_to_replace] = time

# This will insert before requested spot 
# runners.insert(index_to_replace, name)
# times.insert(index_to_replace, time)

for i in range(len(runners)):
    print(f"{i+1}. {runners[i]} - {times[i]}")
    # cur_runner = runners[i]
    # cur_times = times[i]

    # print(f"{cur_runner} - {cur_time}")



