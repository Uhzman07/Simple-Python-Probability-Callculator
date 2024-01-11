"""
import random 
birthdays = [random.randint(1,35) for _ in range (20)]
birthdays2 = set(birthdays)
print(birthdays)
print(f"This are the sets {birthdays2}")
for i in range (len(birthdays)):
    number = birthdays[i]
    desiredPosition = i
    for j in range (len(birthdays)):
        if number == birthdays[j] and j != desiredPosition :
            print(f"This is the common number{number}")
"""
import random

def birthday_simulation(num_simulations, num_people):
    success_count = 0

    for _ in range(num_simulations):
        # Generate random birthdays for each person in the room
        birthdays = [random.randint(1, 365) for _ in range(num_people)]

        # Check if there is at least one pair with the same birthday
        if len(birthdays) != len(set(birthdays)):
        #if(len(birthdays)-len(set(birthdays)) ==0): 
            #print(len(set(birthdays)))
            success_count += 1

    # Calculate the probability
    probability = success_count / num_simulations
    return probability

# Number of simulations and people in the room
num_simulations = 100000
num_people = 30

# Run the simulation
result = birthday_simulation(num_simulations, num_people)

# Print the result
print(f"The estimated probability of a pair of people sharing the same birthday in a room of {num_people} is: {result:.4f}")
