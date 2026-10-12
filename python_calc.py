# Return the sum of two numbers.
def add(a, b):
    return a + b


# Return the difference between two numbers.
def subtract(a, b):
    return a - b


# Return the product of two numbers.
def multiply(a, b):
    return a * b


def divide(a, b):
    # Prevent division by zero.
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def even_odd(n):
    # Check whether a number is even or odd.
    if n % 2 == 0:
        return "Even"
    return "Odd"


def percentage(value, total):
    # Calculate a value as a percentage of the total.
    if total == 0:
        return "Error: Total cannot be zero."
    return (value / total) * 100


while True:
    # Display the menu repeatedly until the user exits.
    print("\nHi! Welcome to the Python Calculator.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add two user-provided numbers.
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == "2":
        # Subtract the second number from the first.
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == "3":
        # Multiply two user-provided numbers.
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == "4":
        # Divide the first number by the second.
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", divide(a, b))

    elif choice == "5":
        # Determine whether the entered number is even or odd.
        n = int(input("Enter a number: "))
        print(n, "is", even_odd(n))

    elif choice == "6":
        # Calculate the percentage of the obtained value.
        value = float(input("Enter obtained value: "))
        total = float(input("Enter total value: "))
        result = percentage(value, total)
        if isinstance(result, str):
            print(result)
        else:
            print("Percentage:", result, "%")

    elif choice == "7":
        # Leave the calculator loop.
        print("Thank you for using the calculator.")
        break

    else:
        # Report an invalid menu selection.
        print("Invalid choice. Please try again.")