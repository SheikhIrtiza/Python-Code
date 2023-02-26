states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia","New York",
    "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
    "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota",
    "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",   
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

dirty_dozen = [
    "Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
    "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"
]

dirty_dozen.append("banana")
dirty_dozen.extend("spinach")
#states_of_america.clear()
dirty_dozen.remove("banana")
#states_of_america.reverse()
dirty_dozen.sort()
states_of_america.sort()

print(dirty_dozen)
print(states_of_america)
