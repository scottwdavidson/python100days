# divisible by 3 ( fizz ), div by 5 ( buzz ), div by both (fizz-buzz)
def fizzbuzz(count):
    response = ""
    if ( count % 3 == 0 ):
        response = "fizz"

    if ( count % 5 == 0 ):
        response += "buzz"

    if ( response == ""):
        response = count
        
    return response

for count in range(1,101):
    print(f"({count}) - {fizzbuzz(count)}")

