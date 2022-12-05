# Open the input file and read the rucksack items
with open('input.txt', 'r') as f:
    rucksack_items = [line.strip() for line in f]

# Compute the sum of the priorities of the common letters in the rucksacks
priority_sum = 0
for items in rucksack_items:
    # Split the items into the two compartments
    compartment1 = items[:len(items)//2]
    compartment2 = items[len(items)//2:]

    # Find the common letter in the compartments
    common_letter = set(compartment1) & set(compartment2)

    # Compute the priority of the common letter
    priority = 0
    for letter in common_letter:
        if letter.islower():
            priority = ord(letter) - ord('a') + 1
        else:
            priority = ord(letter) - ord('A') + 27

    # Add the priority to the running total
    priority_sum += priority

# Print the final result
print(priority_sum)
