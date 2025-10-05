"""Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else
statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something
like, “How about some bacon and eggs? The user may enter something else in, but you only have to respond to breakfast,
lunch, or dinner.
"""

user_meal = input("Which meal are you looking for? Breakfast, lunch, dinner? Select one: ").lower()

if user_meal == "breakfast":
    print("What about some eggs benedict?")
elif user_meal == "lunch":
    print("What about a lamb burger?")
elif user_meal == "dinner":
    print("what about a steak with fries?")
else:
    print("Just have a piece of fruit. It's apple season!")

"""
Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, 
including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their 
regular hourly pay rate for all hours over 20. You should take in the user’s input for the number of hours worked, and 
their rate of pay.
"""

number_hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the rate per hour: "))


def gross_pay(number_hours, rate_per_hour):
    hours = min(number_hours, 20)
    extra_hours = max(0, number_hours - 20)
    return hours * rate_per_hour + extra_hours * rate * 1.5


if number_hours < 0 or rate < 0:
    print("Please enter positive values!")
else:
    salary = gross_pay(number_hours, rate)
    print(f"The gross salary is ${salary:.2f}")

"""
Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument
multiplied times 10.
"""
a = float(input("Enter a number to be multiplied by ten: "))


def times_ten(a):
    print(a * 10)


times_ten(a)

"""
SQ4: Find the errors, debug the program, and then execute to show the output.

def main()
      Calories1 = input( "How many calories are in the first food?")
      Calories2 = input( "How many calories are in the first food?")
      showCalories(calories1, calories2)

def showCalories()   
   print(“The total calories you ate today”, format(calories1 + calories2,.2f))
"""

def main():
    calories1 = float(input("How many calories are in the first food?: "))
    calories2 = float(input("How many calories are in the second food?"))
    show_calories(calories1, calories2)

def show_calories(calories1, calories2):
    total_calories = calories1 + calories2
    print(f"The total calories you ate today {total_calories:.2f}")


main()

# added the colon in the main function. Lower case for vars and functions. Added float to the input for computation.
# format of the output with 2 decimals using string

"""
Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
         1/30 + 2/29 + 3/28 ............. + 30/1
"""
total_series = 0.0

for i in range(1, 31):
    total_series += i / (31 - i)

print(f"The total sum is: {total_series:.5f}")


"""
Q6: Write a function that computes the area of a triangle given its base and height.
The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT

For example, if the base was 5 and the height was 4, the area would be 10.
triangle_area(5, 4)   # should print 10
"""
base = float(input("What is the base of triangle?: "))
height = float(input("What is the height of the triangle: ?"))


def area_triangle(base, height):
    area = 0.5 * base * height
    print(f"The are of the triangle is {area:g}")


if base < 0 or height < 0:
    print("Error: dimensions need to be positive")
else:
    area_triangle(base, height)

