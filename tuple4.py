def modify_tuple(input_tuple):
    # Print the original tuple and its ID
    print("Original tuple:", input_tuple)
    print("ID of original tuple:", id(input_tuple))

    # Convert the tuple to a list
    temp_list = list(input_tuple)
    
    # Remove the 2nd element (index 1)
    del temp_list[1]
    
    # Remove the last element
    del temp_list[-1]
    
    # Convert the list back to a tuple
    modified_tuple = tuple(temp_list)
    
    # Print the modified tuple and its ID
    print("Modified tuple:", modified_tuple)
    print("ID of modified tuple:", id(modified_tuple))
    
# Define the tuple
tuple1 = (2, 7, [5, 7, 8], 'Tutor', True, 'T', 3.21)

# Call the function
modify_tuple(tuple1)
