# Step 1: Create the tuple of tuples by accepting colors from the user
def create_colors_tuple():
    colors = []
    for i in range(3):
        row = []
        for j in range(3):
            color = input(f"Enter color for row {i+1}, column {j+1}: ")
            row.append(color)
        colors.append(tuple(row))
    return tuple(colors)

# Step 2: Function to check if a color exists in the tuple of tuples
def check_color_exists(colors, color_to_check):
    for row in colors:
        if color_to_check in row:
            return True
    return False

# Accept colors from the user to create the tuple of tuples
colors_tuple = create_colors_tuple()

# Print the created tuple of tuples
print("The created tuple of tuples is:")
print(colors_tuple)

# Accept a color from the user to check
color_to_check = input("Enter a color to check if it exists: ")

# Check if the color exists in the tuple of tuples
exists = check_color_exists(colors_tuple, color_to_check)

# Print the result
if (exists):
    print(f"The color {color_to_check} exists in the tuple of tuples.")
else:
    print(f"The color {color_to_check} does not exist in the tuple of tuples.")
