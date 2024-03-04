def reverse_str(my_str):
    if len(my_str) == 0:
        return my_str
    else:
        return reverse_str(my_str[1:]) + my_str[0]


my_string = input('Enter your string:')
print(f"Given String: {my_string}")
print(f"reversed String: {reverse_str(my_string)}")
