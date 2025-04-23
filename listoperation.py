my_list = [4, 5, 6]

# Check if 6 is in the list
if 6 in my_list:
    print("6 is in the list.")
    # Access the value 6
    value = my_list[my_list.index(6)]
    print(f"Accessed value: {value}")
else:
    print("6 is not in the list.")
