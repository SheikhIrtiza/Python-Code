import math

def get_square_root():
    # Ask the user for a number
    number = int(input("Enter a number to find the square root: "))
    # Calculate the square root
    square_root = math.sqrt(number)
    # Check if the square root is an integer
    if square_root.is_integer():
        print(f"The square root of {number} is {int(square_root)}.")
    else:
        print(f"The number {number} is not a perfect square.")

# Call the function
get_square_root()
