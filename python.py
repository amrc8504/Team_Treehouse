#fString
# f_name=input("What is your first name?  ")
# capsName = f_name.title()
# print(f'Hello, {capsName}! Welcome!')

#Puzzle
# def display_blanks(word):
#     blanks = "-" * len(word)
#     print(blanks)

# print("Puzzle 1:")
# display_blanks("treehouse")
# print("Puzzle 2:")
# display_blanks( "python")

# Check for password - while loops
# import sys

# MASTER_PASSWORD = 'opensesame'
# password = input("Please enter your password: ")
# attempts = 1
# while password != MASTER_PASSWORD:
#     if attempts > 3:
#         sys.exit("Too many attempts, please try again later.")
#     password = input("Invalid password, please try again: ")
#     attempts += 1
# print("Welcome to secret town.")

#for loops
# banner = "Happy Birthday!"
# for letter in banner:
#     print(letter.upper())

# Each iteration through the iterable produces the next letter.
# for letter in "You got this!":
#     if letter in "oh":
#         print(letter)

# Lists

# attendees = ['anthony', 'arielle', 'tyler']
# attendees.append("Ashley")
# attendees.extend(["James", "Guil"])
# optional_invites = ["Ben J.", "Dave"]
# potential_attendees = attendees + optional_invites
# attendees.insert(0, "Tony")
# print(attendees)
# print("There are", len(potential_attendees), "attendees currently.") 
anthonys_lunch = "\N{TACO}"
carne_asada = anthonys_lunch
del anthonys_lunch
print(carne_asada)