interest = int(input("Enter the year of interest: "))
print("")
chosen_year = interest

highest_life = 0
highest_country = ""
time_year = 0

lowest_life = 99999
lowest_country = ""
time_age = 99999

highest_life_two = -1
country_two = ""

lowest_life_two= 99999
country_three = ""


with open("life-expectancy.csv") as f:
    next(f)
    for line in f:
        parts = line.split(",")

        # Save each part into a variable
        enity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life = float(parts[3])

        if life > highest_life:
            highest_life = life 
            highest_country = enity
            if year > time_year:
                time_year = year

        if life < lowest_life:
            lowest_life = life
            lowest_country = enity
            if year < time_age:
                time_age = year
        
        if chosen_year == year:
  
            if life > highest_life_two:
                highest_life_two = life
                country_two = enity
            
            if life < lowest_life_two:
                lowest_life_two = life 
                country_three = enity


print(f"The overall max life expectancy is: {highest_life} from {highest_country} in {time_year}.")
print(f"The overall min life expectancy is: {lowest_life} from {lowest_country} in {time_age}.")
print("")

print(f"For the year {interest}:")
# print(f"The average life expectancy across all countries was {average}")
print(f"The max life expectancy was in {country_two} with {highest_life_two}")
print(f"The min life expectancy was in {country_three} with {lowest_life_two}")

        


