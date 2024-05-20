from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charamander"])




print(table)


