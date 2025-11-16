"""
Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
lastname, and balance.
The default balance should be set to 0.
In addition, create ...
● A method called deposit() that allows the user to make deposits into their balance.
● A method called withdrawal() that allows the user to withdraw from their balance.
● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
in your withdrawal() method.
● Use the __str__() method in order to display the bank name, owner name, and current
balance.
● Make a series of deposits and withdrawals to test your class.
"""


class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        """ensure it's a positive amount"""
        if amount > 0:
            self.balance += amount
            print(f"You deposited ${amount:.2f}. Your new balance is: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive. Please, insert a positive amount.")

    def withdrawal(self, amount):
        """Withdrawal a certain amount only if that amount is less or equal than the balance"""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print(f"Your balance is ${self.balance:.2f}, which is less than the withdrawal amount.")
        else:
            self.balance -= amount
            print(f"You withdrew ${amount:.2f}. Your new balance is: ${self.balance:.2f}")

    def __str__(self):
        """String with the bank name, owner's first and last name, and current balance."""
        owner = f"{self.firstname} {self.lastname}"
        return f"Bank: {self.bankname} ; Owner: {owner} ; Balance: ${self.balance:.2f}"

# Test BankAccount class
account = BankAccount("DATA 602 Bank", "Lionel", "Messi")

print(account)


account.deposit(5000)
account.withdrawal(200)
account.withdrawal(5500)
account.deposit(0)
account.withdrawal(-400)
account.deposit(888)
account.withdrawal(1)

print("Final account balance:")
print(account)

"""
Q2: Create a class Box that has attributes length and width that takes values for length
and width upon construction (instantiation via the constructor).
In addition, create…
● A method called render() that prints out to the screen a box made with asterisks of
length and width dimensions
● A method called invert() that switches length and width with each other
● Methods get_area() and get_perimeter() that return appropriate geometric calculations
● A method called double() that doubles the size of the box. Hint: Pay attention to return
value here.
● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
their respective lengths and widths are identical.
● A method print_dim() that prints to screen the length and width details of the box
● A method get_dim() that returns a tuple containing the length and width of the box
● A method combine() that takes another box as an argument and increases the length
and width by the dimensions of the box passed in
● A method get_hypot() that finds the length of the diagonal that cuts through the middle
● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
box2 and box3 respectively
● Print dimension info for each using print_dim()
● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
screen accordingly
● Combine box3 into box1 (i.e. box1.combine())
● Double the size of box2
● Combine box2 into box1
"""


import math


class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        """Print a box made of asterisks with given length and width."""
        # length = number of columns, width = number of rows
        for _ in range(self.width):
            print("*" * self.length)

    def invert(self):
        """Swap length and width."""
        self.length, self.width = self.width, self.length

    def get_area(self):
        """Return the area of the box."""
        return self.length * self.width

    def get_perimeter(self):
        """Return the perimeter."""
        return 2 * (self.length + self.width)

    def double(self):
        """
        Double the size of the dimensions.
        Returning self lets us chain if we want.
        """
        self.length *= 2
        self.width *= 2
        return self

    def __eq__(self, other):
        """Check if the boxes have the same length and width."""
        if not isinstance(other, Box):
            return False
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        """Print length and width information."""
        print(f"Length: {self.length}, Width: {self.width}")

    def get_dim(self):
        """Return (length, width) as a tuple."""
        return (self.length, self.width)

    def combine(self, other):
        """
        Increase this box's dimensions by those of another box.
        Modifies current box.
        """
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        """Return the length of the hypotenuse."""
        return math.hypot(self.length, self.width)


# boxes
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

# dimension info
print("=== Box Dimensions ===")
print("Box 1:")
box1.print_dim()
print("Box 2:")
box2.print_dim()
print("Box 3:")
box3.print_dim()
print()

# compare boxes
print("=== Box Equality Checks ===")
print("box1 == box2 ?", box1 == box2)  # should be False
print("box1 == box3 ?", box1 == box3)  # should be True
print()

# combine box3 into box1
print("=== Combine box3 into box1 ===")
box1.combine(box3)
print("New dimensions of box1 after combining box3:")
box1.print_dim()
print(f"Area: {box1.get_area()}, Perimeter: {box1.get_perimeter()}, Diagonal: {box1.get_hypot():.2f}")
print()

# Double the size of box2
print("=== Double the size of box2 ===")
box2.double()
print("New dimensions of box2:")
box2.print_dim()
print(f"Area: {box2.get_area()}, Perimeter: {box2.get_perimeter()}, Diagonal: {box2.get_hypot():.2f}")
print()

# combine box2 into box1
print("=== Combine box2 into box1 ===")
box1.combine(box2)
print("Final dimensions of box1 after combining box2:")
box1.print_dim()
print(f"Area: {box1.get_area()}, Perimeter: {box1.get_perimeter()}, Diagonal: {box1.get_hypot():.2f}")
print()