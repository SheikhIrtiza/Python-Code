age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

# print(months_remaining)

message = f"you have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."

print(message)
