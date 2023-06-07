def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    # Reverse the string
    reversed_string = string[::-1]
    # Check if the original and reversed strings are equal
    if string == reversed_string: 
        return True
    else:
        return False 
  
# Example usage 
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
