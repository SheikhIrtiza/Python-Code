from prettytable import PrettyTable 
table = PrettyTable()
#Adding methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Adding attributes
table.align = "l"

print(table)
