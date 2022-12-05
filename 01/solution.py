# Open the file and read its contents
with open('input.txt', 'r') as file:
    data = file.read()

# Split the input into groups based on blank lines
groups = data.split("\n\n")

# Sum up the Calories in each group
calories = [sum(map(int, group.split("\n"))) for group in groups]

# Find the group with the maximum Calories
max_calories = max(calories)

# Print the result
print(max_calories)