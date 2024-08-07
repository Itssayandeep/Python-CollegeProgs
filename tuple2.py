# Define the list of tuples
lst_tuples = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

# Convert each tuple in lst_tuples to a list using list comprehension
lst_of_lists = [list(tup) for tup in lst_tuples]

# Print the resulting list of lists
print(lst_of_lists)
