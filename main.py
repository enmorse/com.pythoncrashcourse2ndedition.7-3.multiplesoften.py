# Ask the user to enter a number, and then report
# whether the number is a multiple of 10 or not.
number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"\nThe number {number} is divisible by ten.")

if not (number % 10 == 0):
    print(f"\nThe number {number} is not divisible by "
          f"ten.")
