# Question 1: What will the following code display?
# Answer: The code provided will display an empty list since [1:-5] selects 2nd element as a starting point
# and -5 corresponds to the first element of the list since it only has five elements.

numbers = [1, 2, 3, 4, 5]
print(numbers[:])

# Question 2

store_sales = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in days:
    value = float(input(f"Enter {i} sales value: "))
    store_sales.append(value)

total_sales = sum(store_sales)
print(f"This week sales: {total_sales}")

# Question 3: Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order

places_travel = ["Rio de Janeiro", "Lima", "Bilbao", "Beijing", "Mexico City"]

# Print your list in its original order.
print(places_travel)

# Use the sort() function to arrange your list in order and reprint your list.
places_travel.sort()
print(places_travel)

# Use the sort(reverse=True) and reprint your list.
places_travel.sort(reverse = True)
print(places_travel)


# Question 4: Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.

rooms_course = {
    "D451" : "Room 131",
    "D424" : "Room 031",
    "C878" : "Room 109",
    "C101" : "Room 214",
    "C231" : "Room 121"
}

time_rooms = {
    "D451" : "10:30",
    "D424" : "11:30",
    "C878" : "12:30",
    "C101" : "1:30",
    "C231" : "2:30"
}

instructors = {
    "D451" : "Jonas Sudakov",
    "D424" : "Robert Pires",
    "C878" : "Pierre Cantona",
    "C101" : "Mary Cardozo",
    "C231" : "Nico Klein"
}

user_course = input("Enter the course you are looking for: ").strip().upper()

user_room = rooms_course.get(user_course)
user_time = time_rooms.get(user_course)
user_instructors = instructors.get(user_course)

if user_room and user_time and user_instructors:
    print(f"{user_course} class meets in {user_room} with professor {user_instructors} at {user_time}")
else:
    print(f"Sorry but '{user_course}' is not a listed course")


# Question 5: Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.

contacts = {
    "walter" : "waltertesting@gmail.com",
    "stephen" : "sttesting@gmail.com",
    "anna" : "annatesting@outlook.com",
    "pedro" : "pedrotesting@outlook.com",
    "hayley" : "hayleytesting@yeahoo.com"
}

def user_menu():
    print("\n Menu for users contacts")
    print("1. Look up email")
    print("2. Add more contacts")
    print("3. Update email")
    print("4. Delete contact")
    print("5. Exit")

while True:
    user_menu()
    option = input("Select and option: ").strip()

    if option == "5":
        print("See you soon!")
        break

    elif option == "1":
        name = input("Who do you want to look up for?: ").strip().lower()
        email = contacts.get(name)
        if email:
            print(f"Email for {name}: {email}")
        else:
            print(f"{name} is not part of the list")

    elif option == "2":
        name = input("Enter the contact you want to add: ").strip().lower()
        if name in contacts:
            print("This name already exists!")
        else:
            email = input("What is the email address?: ").strip()
            contacts[name] = email
            print(f"{email} is now {name} email contact")

    elif option == "3":
        name = input("Enter the contact name to update: ").strip().lower()
        if name in contacts:
            email_new = input("Enter the new email address: ").strip()
            contacts[name] = email_new
            print(f"{name.title()} was updated with the {email_new}")
        else:
            print(f"{name.title()} is not in the contact list")

    elif option == "4":
        name = input("Enter the name of the contact you want to delete: ").strip().lower()
        if name in contacts:
            remove = contacts.pop(name)
            print(f"{name.title()} contact was {remove}")
        else:
            print(f"{name.title()} is not in the contact list")

    elif option == "5":
        print("\nAll contacts:")
        for n, e in sorted(contacts.items()):
            print(f"{n.title()}: {e}")

    else:
        print("This option is not valid. Select 0-5")

