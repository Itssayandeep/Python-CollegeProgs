def calculate_averages(nums):
    # Calculate the number of inner tuples
    num_tuples = len(nums)
    
    # Use list comprehension to calculate the averages
    averages = [
        sum(tup[i] for tup in nums) / num_tuples for i in range(3)
    ]
    
    return averages

# Define the tuple
nums = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))

# Call the function and print the result
averages = calculate_averages(nums)
print(averages)
