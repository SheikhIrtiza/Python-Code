#Functions with outputs


def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."#use this instead of none result
  formated_f_name = f_name.title() #f is first name and l is last name.
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
