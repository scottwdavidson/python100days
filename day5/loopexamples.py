def avg_weight(weights):
    weightSum = 0
    for weight in weights:
        weightSum += weight
    return round(int(weightSum / len(weights)))

def max_weight(weights):
    max = weights[0]
    for weight in weights:
        if weight > max:
            max = weight

    return max

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

weights = [150, 145, 190, 166, 188, 114, 201, 166, 134]

print(f"Avg Weight of {weights} is : {avg_weight(weights)}")
print(f"Max Weight ({max_weight(weights)})({max(weights)})")

