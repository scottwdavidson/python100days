from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Artist",["ARS","Seals & Crofts", "Paul McCartney", "Bill Withers"])
table.add_column("Song Title",["So Into You", "Summer Breeze", "Listen To What The Man Said", "Ain't No Sunshine"])
table.align = "l"
print(table)
