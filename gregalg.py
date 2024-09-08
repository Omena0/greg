import re

# Initialize variables to keep track of the line with the most "greg"s
max_greg_line = ""
max_greg_count = 0

i = 0

# Open the file in read mode
with open('greg.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        print(f'Line: {i}')
        # Count the number of "greg"s in the line using regex
        greg_count = len(re.findall(r'\bgreg\b', line))
        
        # If this line has more "greg"s than the previous max, update the max
        if greg_count > max_greg_count:
            max_greg_line = line.strip()
            max_greg_count = greg_count

        i += 1

# Print the line with the most "greg"s
print(max_greg_line)