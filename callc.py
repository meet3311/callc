import sys

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Division by zero.")
        return None

# Function to display calculation history
def display_history(history):
    print("\nCalculation History:")
    for entry in history:
        print(entry)

# Main calculator function
def calculator():
    history = []

    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '6':
            sys.exit("Exiting the calculator app.")

        if choice in {'1', '2', '3', '4'}:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Error: Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                if result is not None:
                    operation = f"{num1} / {num2} = {result}"
                else:
                    continue  # Skip adding the operation to history in case of division by zero

            history.append(operation)
            print(f"Result: {operation}")

        elif choice == '5':
            display_history(history)

        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    calculator()
