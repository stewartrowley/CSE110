people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_person = 9999
youngest_name = "" # It doesn't matter what you set this to, it just needs to be declared

for people_line in people:

    parts = people_line.split()

    name = parts[0] # Product name is the first part
    age = int(parts[1])

    if age < youngest_person:
        # This is the new max
        youngest_person = age

        # Also save this product name as the max product
        youngest_name = name

print(f"The name of the person is: {youngest_name} and there age is {youngest_person}.")