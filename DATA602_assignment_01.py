# Q1 Fix all the syntax and logical errors in the given source code
# add comments to explain your reasoning

# I added a space at the beginning of all comments above and Q2 and Q3 since that is the standard

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

# I changed the high_score variable to lower case to match the high_score var compared with average
high_score = 95
 
# Get the test scores.
# I added the test3 variable to properly calculate the average between 3 testes.
# I also converted the input to a float otherwise we would use a string in a calculation.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))

# Calculate the average test score.
# I added parenthesis bc of order of operations
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is: ', average)

# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')

# This print function below was outside the if condition, so it would always print regardless of the score.
# print('That is a great average!').

# Q2
# The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles
# and prints to the user the area of both rectangles.

# Ask user to input the width and length for both rectangles. Used float to manage decimals if needed
width1 = float(input("What is the width of rectangle 1?: "))
length1 = float(input("What is the length of rectangle 1?: "))
width2 = float(input("What is the width of rectangle 2?: "))
length2 = float(input("What is the length of rectangle 2?: "))

# Calculate area of both rectangles
area1 = width1 * length1
area2 = width2 * length2

# Print the area of both rectangles
print("The are of rectangle 1 is: ", area1)
print("The are of rectangle 2 is: ", area2)

# Q3
# Ask a user to enter their first name and their age and assign it to the variables name and age.
# The variable name should be a string and the variable age should be an int.
name = input("Insert your first name: ")
age = int(input("Insert your age: "))

# Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print(f"Happy birthday, {name}! You are {age} years old today!")

