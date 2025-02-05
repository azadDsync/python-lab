
variable_name = input("Enter a variable name: ")


if variable_name.isidentifier():
    print("Valid variable name.")
else:
    print("Invalid variable name. Variable names must start with a letter or underscore and contain only letters, numbers, and underscores.")
