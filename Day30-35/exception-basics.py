# FILE ERROR
# with open("a_file.json") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    value = a_dictionary["key"]
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("this is a dummy line")
except KeyError as key_error_message:
    print(f"That key {key_error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()


# KEY ERROR
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non-existent-key"]

# INDEX ERROR
# fruit_list = ["Apple", "Pear", "Orange"]
# fruit = fruit_list[3]

# TYPE ERROR
# text = "abc"
# print(text + 5)