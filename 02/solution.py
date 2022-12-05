import sys

file = open('input.txt', 'r')
data = file.read()
lines = data.split('\n')
lines.pop()

# dictionary to map letters to their corresponding numbers
mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

total_score = 0

for line in lines:
    # get the number of the shape chosen by your opponent and you
    opponent_shape = mapping[line[0]]
    my_shape = mapping[line[2]]

    # calculate the score of the round
    score = 0
    if my_shape == opponent_shape:
        score = 3 + my_shape
    elif (my_shape == 1 and opponent_shape == 3) or (my_shape == 2 and opponent_shape == 1) or (my_shape == 3 and opponent_shape == 2):
        score = 6 + my_shape
    else:
        score = 0 + my_shape

    # add the round score to the total score
    total_score += score
    
print(total_score)

file.close()
