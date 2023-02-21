from prettytable import PrettyTable #install the package first
table = PrettyTable()
#Adding methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("type2", ["a", "b", "c"])#we can add more no. of columns 

#Adding attributes
table.align = "l"

print(table)
