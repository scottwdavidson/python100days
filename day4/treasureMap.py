row0 = [" "," "," "]
row1 = [" "," "," "]
row2 = [" "," "," "]
print(f"{row0}\n{row1}\n{row2}")

inputMapPosition = input("Where do you want to check? (row , col)?\n")
mapPosition = inputMapPosition.split(",")
row = int(mapPosition[0])
col = int(mapPosition[1])

if 0 == row:
    row0[col] = "X"
elif 1 == row:
    row1[col] = "X"
else:
    row2[col] = "X"

print(f"{row0}\n{row1}\n{row2}")


