def range_contains(r1, r2):
    # Check if range r1 contains range r2
    start1, end1 = r1
    start2, end2 = r2
    return start1 <= start2 and end1 >= end2

with open('input.txt') as f:
    # Read input lines
    lines = f.readlines()

counter = 0

for line in lines:
    # Split line into ranges
    ranges = line.split(',')
    range1 = tuple(map(int, ranges[0].split('-')))
    range2 = tuple(map(int, ranges[1].split('-')))

    # Check if range1 contains range2 or range2 contains range1
    if range_contains(range1, range2) or range_contains(range2, range1):
        counter += 1
print(counter)
