# -------------------------------
# Python Variables Assignment
# -------------------------------

# 1. What is a variable?
# A variable is a name that represents a location in memory where data is stored.
# The value stored in a variable can change while the program is running.


# 2. Variable name examples
x = 10
july2009 = 2009
theSalesFigureForFiscalYear = 50000
grade_report = "A"

# Illegal variable names (shown as comments because they cause errors):
# 99bottles = 99       # Cannot start with a number
# r&d = 5              # Special characters like & are not allowed


# 3. Prompt the user to enter a customer's last name
last_name = input("Enter the customer's last name: ")


# 4. Display personal information
print("\n--- Personal Information ---")
print("Name: Shola")
print("Address: 1500 Havenwood Rd, Baltimore, MD 21218")
print("Phone Number: 555-555-5555")
print("College Major: Information Technology")


# 5. Celsius to Fahrenheit Temperature Converter
print("\n--- Celsius to Fahrenheit Converter ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print("Temperature in Fahrenheit:", fahrenheit)
