# ask for the informatiom
name = input("What is the speaker's name? ")
# name = input('What is the speaker\'s name')
date = input("What is the date? ")
topic = input("What is the topic? ")
company = input("What is the company ")

# display it, formatted like a poster
print(name.upper())
print(f"From: {company.title()}")
print(f"Department Forum - {date}")
print(f"Topic: {topic.title()}")